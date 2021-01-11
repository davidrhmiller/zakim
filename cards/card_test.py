import unittest

class TestCard(unittest.TestCase):
  def test_init(self):
    try:
      Card(7, 'H')
      Card(10, 'D')
      Card('Q', 'S')
      Card('9', 'D')
      Card(13, 'C')
      Card(1, 'C')
    except ExceptionType:
      self.fail('Card() raised ExceptionType unexpectedly!')
    
    with self.assertRaises(ValueError):
      print(Card(23, 'D'))
    with self.assertRaises(ValueError):
      print(Card(7, 'F'))
    with self.assertRaises(ValueError):
      print(Card(0, 'C'))
    with self.assertRaises(ValueError):
      print(Card(14, 'C'))

  def test_rank_name(self):
    self.assertEqual(Card(1, 'D').rank_name(), 'A')
    self.assertEqual(Card(5, 'D').rank_name(), '5')
    self.assertEqual(Card(10, 'D').rank_name(), 'T')
    self.assertEqual(Card(11, 'D').rank_name(), 'J')
    self.assertEqual(Card(12, 'D').rank_name(), 'Q')
    self.assertEqual(Card(13, 'D').rank_name(), 'K')

  def test_rank(self):
    self.assertEqual(Card(5, 'D').rank(), 3)
    self.assertEqual(Card('5', 'D').rank(), 3)
    self.assertEqual(Card(10, 'D').rank(), 8)
    self.assertEqual(Card('T', 'D').rank(), 8)
    self.assertEqual(Card(11, 'D').rank(), 9)
    self.assertEqual(Card('J', 'D').rank(), 9)
    self.assertEqual(Card(12, 'D').rank(), 10)
    self.assertEqual(Card('Q', 'D').rank(), 10)
    self.assertEqual(Card(13, 'D').rank(), 11)
    self.assertEqual(Card('K', 'D').rank(), 11)
    self.assertEqual(Card(1, 'D').rank(), 12)
    self.assertEqual(Card('A', 'D').rank(), 12)

  def test_suit(self):
    self.assertEqual(Card('A', 'D').suit(), 'D')
    self.assertEqual(Card(3, 'C').suit(), 'C')

  def test_str(self):
    #FMB:  these are backwards, see Card.__str__ comment
    self.assertEqual(str(Card(3, 'H')), 'H3')
    self.assertEqual(str(Card(1, 'S')), 'SA')
    self.assertEqual(str(Card(10, 'D')), 'DT')

  def test_id(self):
    self.assertEqual(Card('2', 'C').id(), 0)
    self.assertEqual(Card('A', 'C').id(), 12)
    self.assertEqual(Card(3, 'D').id(), 14)
    self.assertEqual(Card(9, 'H').id(), 33)
    self.assertEqual(Card('2', 'S').id(), 39)
    self.assertEqual(Card('A', 'S').id(), 51)

  def test_from_id(self):
    for n in range(52):
      self.assertEqual(Card.from_id(n).id(), n)
    for rank_name in ('A', 2, 3, 4, 5, 6, 7, 8, 9, 'T', 'Q', 'K'):
      for suit_name in ('C', 'D', 'H', 'S'):
        card = Card(rank_name, suit_name)
        self.assertEqual(card, Card.from_id(card.id())) 