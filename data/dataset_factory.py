from zakim.cards import Deal
import tensorflow as tf

def from_lead_rule(batch_size, lead_rule):
  '''Creates a Dataset of hands and leads in batches.
  
  Returns a tf.data.Dataset of tuples of a rank-2 tensor of shape
  [batch_size, 52], and a rank-1 tensor of shape [batch_size]. The
  first tensor is the deal and the second tensor is the position
  of the lead card in West's hand.
  '''
  def my_gen():
    rule = lead_rule()
    while True:
      deal = Deal.create_random()
      lead = rule.get_lead(deal)
      yield (deal.card_ids(), lead)

  return tf.data.Dataset.from_generator(
    my_gen, output_signature=(
      tf.TensorSpec(shape=(52, ), dtype=tf.int8),
      tf.TensorSpec(shape=(), dtype=tf.int8))).batch(batch_size)