from constants.constants import CARD_SUITS

class Card:
  def __init__(self, id, value, suit_id):
    self.id = id
    self.value = value
    self.suit_id = suit_id
    self.suit_symbol = CARD_SUITS[suit_id]
    
  def format_card(self):
    return f"{self.value}{self.suit_symbol}"