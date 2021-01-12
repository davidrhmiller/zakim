class LeadRule:
  def __init__(self):
    return

  @classmethod
  def get_lead(cls, deal):
    '''Returns an index in [0, 12] of a card in West's hand to lead.'''
    raise NotImplementedError("Override this method and write a rule.")
