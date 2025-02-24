from assets.entities.monster_card import MonsterCard
from assets.entities.potion_card import PotionCard
from assets.entities.weapon_card import WeaponCard
from constants.constants import CARD_SUITS, CARD_VALUES
from engine.deck import Deck


class ScoundrelDeck(Deck):
  def __init__(self):
    self.cards = self.generate_scoundrel_cards()
    self.shuffle()
    
  def generate_scoundrel_cards(self):
    cards = []
    
    for suit in CARD_SUITS:
      match suit:
        case 0:
          self.add_monsters(cards, suit)
        
        case 1:
          self.add_potions(cards, suit)
          
        case 2:
          self.add_weapons(cards, suit)
          
        case 3:
          self.add_monsters(cards, suit)
          
        case _:
          return
        
    return cards

  def add_monsters(self, cards, suit):
    card_id = len(cards) + 1
    
    for value in CARD_VALUES:
      cards.append(MonsterCard(card_id, value, suit))

  
  def add_potions(self, cards, suit):
    card_id = len(cards) + 1
    
    for value in CARD_VALUES:
      cards.append(PotionCard(card_id, value, suit))
    
  def add_weapons(self, cards, suit):
    card_id = len(cards) + 1
    
    for value in CARD_VALUES:
      cards.append(WeaponCard(card_id, value, suit))