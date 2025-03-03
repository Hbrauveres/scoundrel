from constants.constants import ACTION_MESSAGE_BY_TYPE
from engine.card import Card

class EntityCard(Card):
  def __init__(self, id, value, suit, type):
    super().__init__(id, value, suit)
    
    self.type = type
    self.action_text = ACTION_MESSAGE_BY_TYPE[type]
    self.effective_value = int(self.get_effective_value(value))

  def get_effective_value(self, value):
    values = {'A': 14, 'K': 12, 'Q': 11, 'J': 10}
    
    if value in values:
      return values.get(value)
    
    return value