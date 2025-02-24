from engine.card import Card

class EntityCard(Card):
  def __init__(self, id, value, suit, type):
    super().__init__(id, value, suit)
    
    self.type = type
    self.effective_value = self.parse_effective_value(value)

  def parse_effective_value(self, value):
    values = {'A': 14, 'K': 12, 'Q': 11, 'J': 10}
    
    if value in values:
      return values.get(value)
    
    return value