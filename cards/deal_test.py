import unittest

from cards import Deal

class TestDeal(unittest.TestCase):
  def test_init(self):
    deal = Deal(list(range(0, 13)),
                list(range(13, 26)),
                list(range(26, 39)),
                list(range(39, 52)))
    self.assertEqual(13, deal.south.len())
    self.assertEqual(13, deal.west.len())
    self.assertEqual(13, deal.north.len())
    self.assertEqual(13, deal.east.len())

  def test_from_card_ids(self):
    d1 = Deal(list(range(0, 13)),
              list(range(13, 26)),
              list(range(26, 39)),
              list(range(39, 52)))
    d2 = Deal.from_card_ids(list(range(0, 52)))
    self.assertEqual(d1, d2, 'Expected\n{}\n\n got\n{}'.format(
        str(d1), str(d2)))
                                        
  def test_create_random(self):
    deal = Deal.create_random()
    self.assertEqual(13, deal.south.len())
    self.assertEqual(13, deal.west.len())
    self.assertEqual(13, deal.north.len())
    self.assertEqual(13, deal.east.len())
