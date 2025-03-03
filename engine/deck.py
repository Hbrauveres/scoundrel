import random

from engine.card import Card
from constants.constants import CARD_SUITS, CARD_VALUES

class Deck:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Deck, cls).__new__(cls)
            cls._instance._initialize_deck()
        return cls._instance
    
    def _initialize_deck(self):
        self.cards = self.generate_cards()
        self.shuffle()
    
    def generate_cards(self):
      cards = [
          Card(card_id, value, suit) 
          for card_id, (suit, value) in enumerate(
              (suit, value) for suit in CARD_SUITS.keys() for value in CARD_VALUES
          )
        ]
      
      return cards
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop(0) if self.cards else None
      
    def place_on_the_bottom(self, card):
      self.cards.append(card)