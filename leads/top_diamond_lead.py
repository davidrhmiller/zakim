from leads.lead_rule import LeadRule

from cards import Card

class TopDiamondLead(LeadRule):
  '''West always leads their top diamond.

  If West has a Diamond void, they lead their top card in their top-ranked suit.
  '''

  def get_lead(cls, deal):
    # This implementation relies on the cards in West's hand being reverse
    # sorted by card id.
    card_ids = deal.west.card_ids
    for pos, card_id in enumerate(card_ids):
      if Card.from_id(card_id).suit() == "D":
        return pos
    # No diamonds, return the top card in the top-ranked suit.
    return 0