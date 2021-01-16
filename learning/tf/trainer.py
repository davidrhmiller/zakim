import tensorflow as tf

class Trainer:
  def __init__(self,
               model,
               loss_function,
               optimizer,
               checkpoint_manager=None):
    self._model = model
    self._loss_function = loss_function
    self._optimizer = optimizer
    self._checkpoint_manager = checkpoint_manager

  def grad(self, inputs, targets):
    with tf.GradientTape() as tape:
      outputs = self._model(inputs)
      loss_value = self._loss_function(targets, outputs)
    return loss_value, tape.gradient(
        loss_value, self._model.trainable_variables)

  def maybe_save_checkpoint(self, global_step, force=False):
    if self._checkpoint_manager:
      if force or global_step.numpy() % self._checkpoint_manager.checkpoint_interval == 0:
        self._checkpoint_manager.save()
        print("Saved checkpoint for step {} to directory {}".format(
          global_step.numpy(),
          self._checkpoint_manager.directory))


  def train(self, dataset_iterator, num_steps_to_train, steps_between_reports):
    if self._checkpoint_manager:
      if self._checkpoint_manager.latest_checkpoint:
        print("Restoring from {}".format(
          self._checkpoint_manager.latest_checkpoint))
      else:
        print("Initializing from scratch.")
      self._checkpoint_manager.restore_or_initialize()
      
    # Keep results for plotting, one point per 'epoch'
    train_loss_results = []
    train_accuracy_results = []

    # this is arbitrary, makes more sense when data is limited.
    batches_per_epoch = 32
    if self._checkpoint_manager:
      global_step = self._checkpoint_manager.checkpoint.global_step
    else:
      global_step = tf.Variable(1)
    steps_since_last_report = 0
    while global_step < num_steps_to_train:
      # Run one epoch of training
      epoch_loss_avg = tf.keras.metrics.Mean()
      epoch_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()

      # Training loop
      for batch_num in range(batches_per_epoch):
        features, labels = dataset_iterator.next()
        # Optimize the model
        # verbose = (epoch % 20 == 0 and batch_num == 0)
        verbose=False
        loss_value, grads = self.grad(features, labels)
        self._optimizer.apply_gradients(zip(grads, self._model.trainable_variables))

        # Track progress
        epoch_loss_avg.update_state(loss_value)  # Add current batch loss
        epoch_accuracy.update_state(labels, self._model(features))  #FMB: move earlier!
        global_step.assign_add(1)
        steps_since_last_report += 1
        self.maybe_save_checkpoint(global_step)
        if global_step.numpy() % steps_between_reports == 0:
          print('After global step {:05d}: Loss: {:.3f}, Accuracy: {:.3%}'.format(
          global_step.numpy(),
          epoch_loss_avg.result(),
          epoch_accuracy.result()))
          steps_since_last_report = 0


      # End epoch
      train_loss_results.append(epoch_loss_avg.result())
      train_accuracy_results.append(epoch_accuracy.result())        

    self.maybe_save_checkpoint(global_step, force=True)
    print('All done!')
    return train_loss_results, train_accuracy_results
