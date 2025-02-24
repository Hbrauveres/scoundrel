from assets.entity_card import EntityCard
from constants.constants import MONSTER

class MonsterCard(EntityCard):
  def __init__(self, id, value, suit):
    super().__init__(id, value, suit, MONSTER)