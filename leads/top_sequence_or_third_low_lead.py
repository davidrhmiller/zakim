from leads.lead_rule import LeadRule

from numpy import sign
from cards import Card

class TopSequenceOrThirdLowLead(LeadRule):
  ''' A tolerably realistic and complicated leading rule:

  lead top of a sequence or interior sequence such as Ak, Kq, kJt if available
  otherwise lead 3rd highest card from even length and lowest card from odd length.
  '''

  def _pick_lead(cls, ranks):
    '''Given a list of ranks in one suit, choose the rank we would lead
    Doesn't pay attention to contract or auction.  
    2nd return value is an attempted score
    '''

    if len(ranks) == 0:
      return -1  # better not pick this it's not a real rank
    elif len(ranks) < 3 or (ranks[0]>7 and ranks[1] == ranks[0]-1):
      return ranks[0]  # lead singleton or top of any doubleton or top of touching honors
    elif ranks[1] > 7 and ranks[2] == ranks[1]-1:
      return ranks[1]  # interior sequence; might exclude AJT etc vs suit though
    elif len(ranks) % 2 == 0:
      return ranks[2]  # 3rd from even, even if headed by an ace
    else:
      return ranks[-1] # low from odd
      
  def _compare_tuple(cls, t1, t2):
    ''' lazy to put this here, probably lazy to write myself'''
    try:
      for a,b in zip(t1, t2):
        if a==b:
          continue
        else:
          return sign(a - b)
      return 0
    except:
      return 0

  def get_lead(cls, deal):
    card_ids = deal.west.card_ids
    suit_holdings = [list(), list(), list(), list()]
    for id in card_ids:
      card = Card.from_id(id)
      suit_holdings[card.suit_id].append(card.rank_id)
    
    best_lead = None
    best_score = (0,0,0)
    for suit,ranks in enumerate(suit_holdings):
      candidate_rank = cls._pick_lead(ranks)
      # this scoring tries to select longest suit
      score = (len(ranks), candidate_rank, sum(ranks))
      if cls._compare_tuple(score, best_score) == 1:
        best_score = score
        best_lead = Card(Card.RANK_NAME_FROM_RANK_ID[candidate_rank], Card.SUIT_NAME_FROM_SUIT_ID[suit])  #needs smarter constructor
      
    lead_id = best_lead.id()
    lead_position = card_ids.index(lead_id)
    
    return lead_position

