from assets.entity_card import EntityCard


class MonsterCard(EntityCard):
  def __init__(self, id, value, suit):
    super().__init__(id, value, suit, "Monster")