import unittest

from cards import Hand

class TestHand(unittest.TestCase):
  def test_init(self):
    for size in (8, 13, 24):      
      hand = Hand(list(range(size)))
      self.assertEqual(size, hand.len())

    self.assertEqual('S:- H:- D:- C:65432', str(Hand([0, 1, 2, 3, 4])))
    self.assertEqual('S:- H:- D:- C:65432', str(Hand([2, 1, 4, 0, 3])))
    self.assertEqual('S:AKQJT H:- D:- C:-', str(Hand([51, 50, 49, 48, 47])))
    self.assertEqual('S:A H:A D:A C:A', str(Hand([12, 25, 38, 51])))

  def test_create_random(self):
    self.assertEqual(13, Hand.create_random().len())