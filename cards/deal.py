import random
from cards.card import Card
from cards.hand import Hand

class Deal:
  # TODO: Add dealer, vulnerability, maybe board number.  
  #     FMB: TODO: Scoring, Event, Players?  maybe elsewhere?  Partial hands?
  #     FMB: TODO:  Converters to/from std formats PBN, LIN, etc.
  def __init__(self, south_hand, west_hand, north_hand, east_hand):
    '''Creates a deal from 4 explicit hand listings.

    Each hand parameter is simply a list of integers, representing card ids.
    There is no enforcement here that the card ids are distinct,
    or that they are in the range [0, 51], or that there are 13
    cards in each hand.
    '''
    self.south = Hand(south_hand)
    self.west = Hand(west_hand)
    self.north = Hand(north_hand)
    self.east = Hand(east_hand)

  @classmethod
  def from_card_ids(cls, card_ids):
    return cls(card_ids[0:13], card_ids[13:26],
               card_ids[26:39], card_ids[39:52])

  def card_ids(self):
    return self.south.card_ids + self.west.card_ids + self.north.card_ids + self.east.card_ids

  def __str__(self):
    out = '{:>40}\n\n'.format(str(self.north))
    out += '{:27}    {:27}\n\n'.format(str(self.west), str(self.east))
    out += '{:>40}\n'.format(str(self.south))
    return out

  def __eq__(self, other):
    return (self.south == other.south and
    self.west == other.west and
    self.north == other.north and
    self.east == other.east)

  @classmethod
  def create_random(cls):
    deck = list(range(52))
    random.shuffle(deck)
    return cls.from_card_ids(deck)
