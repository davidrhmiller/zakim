# This is patterned after the [TensorFlow custom training tutorial]
# (https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough#define_the_loss_and_gradient_function).

def plot_training_experiment(train_loss_results, train_accuracy_results):
  fig, axes = plt.subplots(2, sharex=True, figsize=(12, 8))
  fig.suptitle('Training Metrics')

  axes[0].set_ylabel("Loss", fontsize=14)
  axes[0].plot(train_loss_results)

  axes[1].set_ylabel("Accuracy", fontsize=14)
  axes[1].set_xlabel("Epoch", fontsize=14)
  axes[1].plot(train_accuracy_results)
  plt.show()