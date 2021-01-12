from cards import Card
from leads.lead_rule import LeadRule

class HighestCardLead(LeadRule):
  '''West always leads their highest card, suit is tie-breaker.'''

  def get_lead(cls, deal):
    # This implementation relies on the cards in West's hand being reverse
    # sorted by card id.
    card_ids = deal.west.card_ids
    best_pos = 0
    best_rank = -1
    for pos, card_id in enumerate(card_ids):
      rank = Card.from_id(card_id).rank()
      # Since this is strictly greater, and we encounter the higher valued
      # suits first, we get the tiebreaker we want.
      if rank > best_rank:
        best_pos = pos
        best_rank = rank
    return best_pos