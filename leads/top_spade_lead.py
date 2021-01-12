from leads.lead_rule import LeadRule

class TopSpadeLead(LeadRule):
  '''West always leads their top spade.

  If West has a spade void, they lead their top card in their top-ranked suit.
  '''

  def get_lead(cls, deal):
    # Since West's hand is always sorted by reversed card id, and card ids are
    # implemented consistent with suit order, West always returns the first
    # card id in their list, that is the 12th item.
    return 0