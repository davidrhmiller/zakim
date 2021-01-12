import unittest

class TestTopSequenceOrThirdLowLead(unittest.TestCase):
  def test_get_lead(self):
    deal = Deal([], range(40, 52), [], [])
    lead = TopSequenceOrThirdLowLead().get_lead(deal)
    self.assertEqual(lead, 0)


# This is odd. Write a unit test for it.
# I think it's a bug.
#
#
#               S:AT52 H:AT74 D:984 C:T6

# S:KJ764 H:Q8 D:AK2 C:AQ7       S:Q98 H:J62 D:QJ76 C:954   

#                 S:3 H:K953 D:T53 C:KJ832

# Lead: S4