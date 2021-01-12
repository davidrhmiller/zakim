from cards import Card

class Example:
  # TODO: add an auction to this
  def __init__(self, deal, lead):
    '''Create an example of the lead prediction problem.

    deal is a Deal object.
    lead is an integer in [0, 12] representing the index
    of the card_id within Deal.west that is lead. This enforces the
    constraint that the card lead must be in West's hand, as is typically the
    case in presentations of hands. 

    Lead may be None for an inference example.'''

    self.deal = deal
    self.lead = lead

  def lead_card_id(self):
    return self.deal.west.card_ids[self.lead]

  @classmethod
  def create_random(cls):
    deal = Deal.create_random()
    lead = random.randrange(13)
    return cls(deal, lead)

  def __str__(self):
    out = str(self.deal)
    out += '\nLead: {}'.format(str(Card.from_id(self.lead_card_id())))
    return out