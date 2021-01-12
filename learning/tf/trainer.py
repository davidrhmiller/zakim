import tensorflow as tf

class Trainer:
  def __init__(self, model, loss_function, optimizer):
    self._model = model
    self._loss_function = loss_function
    self._optimizer = optimizer

  def grad(self, inputs, targets, print_predictions=False):
    with tf.GradientTape() as tape:
      loss_value = self._loss_function(self._model, inputs, targets,
                        print_predictions=print_predictions)
    return loss_value, tape.gradient(
        loss_value, self._model.trainable_variables)
  
  def train(self, dataset_iterator, num_steps_to_train, steps_between_reports):
    # Keep results for plotting, one point per 'epoch'
    train_loss_results = []
    train_accuracy_results = []

    # this is arbitrary, makes more sense when data is limited.
    batches_per_epoch = 32
    global_steps = 0
    steps_since_last_report = 0
    while global_steps < num_steps_to_train:
      # Run one epoch of training
      epoch_loss_avg = tf.keras.metrics.Mean()
      epoch_accuracy = tf.keras.metrics.SparseCategoricalAccuracy()

      # Training loop
      for batch_num in range(batches_per_epoch):
        features, labels = dataset_iterator.next()
        # Optimize the model
        # verbose = (epoch % 20 == 0 and batch_num == 0)
        verbose=False
        loss_value, grads = self.grad(
            features, labels, print_predictions=verbose)
        self._optimizer.apply_gradients(zip(grads, self._model.trainable_variables))

        # Track progress
        epoch_loss_avg.update_state(loss_value)  # Add current batch loss
        epoch_accuracy.update_state(labels, self._model(features))  #FMB: move earlier!
        global_steps += 1
        steps_since_last_report += 1

      # End epoch
      train_loss_results.append(epoch_loss_avg.result())
      train_accuracy_results.append(epoch_accuracy.result())      

      if steps_since_last_report > steps_between_reports:
        print('After global step {:05d}: Loss: {:.3f}, Accuracy: {:.3%}'.format(
            global_steps,
            epoch_loss_avg.result(),
            epoch_accuracy.result()))
        steps_since_last_report = 0

    print('All done!')
    return train_loss_results, train_accuracy_results