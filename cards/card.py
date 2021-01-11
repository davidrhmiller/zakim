class Card:
  # Simpler than calculating these
  RANK_ID_FROM_STRING = {'2': 0, '3': 1, '4': 2, '5': 3,
                      '6': 4, '7': 5, '8': 6, '9': 7, '10': 8, 'T': 8,
                      'J': 9, '11': 9, 'Q': 10, '12': 10, 'K': 11,
                      '13': 11, 
'1': 12, 'A': 12, }
  RANK_NAME_FROM_RANK_ID = ['2', '3', '4', '5', '6', '7', '8', '9',
                            'T', 'J', 'Q', 'K', 'A']

  # Should probably use enums for this.
  SUIT_ID_FROM_STRING = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
  SUIT_NAME_FROM_SUIT_ID = ['C', 'D', 'H', 'S']

  def __init__(self, rank, suit):
    self.rank_id = self.RANK_ID_FROM_STRING.get(str(rank))
    self.suit_id = self.SUIT_ID_FROM_STRING.get(str(suit))
    if self.rank_id is None or self.suit_id is None:
      raise ValueError("Bad card specification")

  def id(self):
    return 13 * self.suit_id + self.rank_id

  @classmethod
  def from_id(cls, card_id):
    # This is a little silly, going from rank id to rank name and then
    # having __init__() go right back to rank id, but I wanted to leave
    # __init__ in terms of string-like things to preservce the canonical
    # Card(7, 'H') call to get the seven of hearts.
    #
    # I don't expect from_id() to be called in performance-sensitive contexts,
    # so I don't mind this being slow.
    return cls(cls.RANK_NAME_FROM_RANK_ID[card_id % 13],
               cls.SUIT_NAME_FROM_SUIT_ID[card_id // 13])

  def suit(self):
    return self.SUIT_NAME_FROM_SUIT_ID[self.suit_id]

  def rank(self):
    return self.rank_id

  def rank_name(self):
    return self.RANK_NAME_FROM_RANK_ID[self.rank_id]

  def __str__(self):
    return self.suit() + self.rank_name()  #FMB:  This is backwards, 7H is a bid, H7 is a card

  def __eq__(self, other):
    return self.rank_id == other.rank_id and self.suit_id == other.suit_id