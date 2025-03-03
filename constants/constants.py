MAX_PLAYER_HEALTH = 20
MAX_ROOM_SLOTS = 4
CARD_SUITS = { 0:'♠', 1:'♥', 2:'♦', 3:'♣' }
CARD_VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUIT_TO_ENTITY = { 0: 'Monster', 1: 'Potion', 2: 'Weapon', 3: 'Monster' }
WEAPON = "Weapon"
POTION = "Potion"
MONSTER = "Monster"
ATTACK_MONSTER_MESSAGE = "Attack Monster"
USE_POTION_MESSAGE = "Use Potion"
EQUIP_WEAPON_MESSAGE = "Equip Weapon"
ACTION_MESSAGE_BY_TYPE = {
  WEAPON: EQUIP_WEAPON_MESSAGE,
  POTION: USE_POTION_MESSAGE,
  MONSTER: ATTACK_MONSTER_MESSAGE
}
CHAR_TO_BOOL = {
  'y': True,
  'n': False
}