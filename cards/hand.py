import random
from cards.card import Card

class Hand:
  def __init__(self, card_ids):
    self.card_ids = card_ids
    self.card_ids.sort(reverse=True)

  def len(self):
    return len(self.card_ids)

  def __str__(self):
    holdings = {'S': list(), 'H': list(), 'D': list(), 'C': list()}
    for id in self.card_ids:
      card = Card.from_id(id)
      holdings[card.suit()].append(card.rank_name())
    suit_strings = dict()
    for suit in ['S', 'H', 'D', 'C']:
      if holdings[suit]:
        suit_strings[suit] = ''.join(holdings[suit])
      else:
        suit_strings[suit] = '-'
    
    return 'S:{} H:{} D:{} C:{}'.format(*[
        suit_strings.get(suit, '-') for suit in ['S', 'H', 'D', 'C']])
  
  def __eq__(self, other):
    return self.card_ids == other.card_ids

  @classmethod
  def create_random(cls):
    deck = list(range(52))
    random.shuffle(deck)
    return cls(deck[0:13])
