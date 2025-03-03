from game.assets.entity_card import EntityCard
from constants.constants import CARD_SUITS, CARD_VALUES, SUIT_TO_ENTITY
from engine.deck import Deck

class ScoundrelDeck(Deck):
  def __init__(self):
    self.cards = self.generate_scoundrel_cards()
    self.shuffle()
    
  def generate_scoundrel_cards(self):
    cards = []
    
    for suit in CARD_SUITS:
      entity_type = SUIT_TO_ENTITY[suit]
      self.add_cards(cards, suit, entity_type)

    return cards

  def add_cards(self, cards, suit, entity_type):
    card_id = len(cards) + 1
    
    for value in CARD_VALUES:
      cards.append(EntityCard(card_id, value, suit, entity_type))