import tensorflow as tf

class LeadModelV0(tf.keras.Model):
  NUM_CARDS = 52
  NUM_WEST_CARDS = 13
  def __init__(self):
    # See https://www.tensorflow.org/tutorials/text/word_embeddings#using_the_embedding_layer
    # for an explainer.
    super(LeadModelV0, self).__init__()
    self._card_embedding_dimension = 128
    # [B, 52] -> [B, 52, M]
    self._card_embedding_layer = tf.keras.layers.Embedding(
        self.NUM_CARDS, self._card_embedding_dimension)

    # [B, 52, M] --> [B, K]
    self._deal_size = 256
    self._deal_embeddings_layer = tf.keras.layers.experimental.EinsumDense(
      'bcm,cmk->bk', output_shape=self._deal_size)
    self._hidden_size = 512
    self._dense_layer = tf.keras.layers.Dense(
        self._hidden_size, activation='relu')
    self._logits_layer = tf.keras.layers.Dense(
        self.NUM_WEST_CARDS, activation='relu')

  def call(self, inputs):
    # print('Inputs: ' + str(inputs.shape))
    # print('Inputs: ' + str(inputs))

    card_embeddings = self._card_embedding_layer(inputs)
    # print('Card Embeddings: ' + str(card_embeddings.shape))
    # print('Card Embeddings: ' + str(card_embeddings))

    # TODO(drm): Make this a self-attention layer.
    #
    # TODO: consider making a hand_embedding where we generate a representation
    # of each of the 4 hands before further collapsing to a vector representing
    # the whole deal.
    #
    # Maybe do this with some reshapes to enforce the hand partitions.

    deal_embeddings = self._deal_embeddings_layer(card_embeddings)
    # print('Deal Embeddings: ' + str(deal_embeddings.shape))
    # print('Deal Embeddings: ' + str(deal_embeddings))

    hidden = self._dense_layer(deal_embeddings)
    # print('Hidden: ' + str(hidden.shape))
    # print('Hidden: ' + str(hidden))

    logits = self._logits_layer(hidden)
    # print('Logits: ' + str(logits.shape))
    # print('Logits: ' + str(logits))
    return logits