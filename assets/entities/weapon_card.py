from assets.entity_card import EntityCard


class WeaponCard(EntityCard):
  def __init__(self, id, value, suit):
    super().__init__(id, value, suit, "Weapon")