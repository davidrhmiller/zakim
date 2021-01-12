import tensorflow as tf

class VerboseLoss:
  '''Wraps a standard loss function with some print calls.'''
  def __init__(self, loss, print_predictions=False):
    self._loss = loss
    self._print_predictions = print_predictions

  def __call__(self, y_true, y_pred, sample_weight=None):
    if self._print_predictions:
      print("Max Logits: {}".format(tf.reduce_max(y_pred, axis=1)))
      print("Best index: {}".format(tf.argmax(y_pred, axis=1)))
      print("    Labels: {}".format(y_true))
    return self._loss(y_true, y_pred, sample_weight)
