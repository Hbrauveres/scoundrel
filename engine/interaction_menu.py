class InteractionMenu:
  def __init__(self, dungeon_room, player):
    self.dungeon_room = dungeon_room
    self.player = player
  
  def AttackDialog(self, card):
    pass
  
  def UsePotionDialog(self, card):
    pass
  
  def AreYouSureDialog(self, card):
    pass
  
  def DisplayPlayerOptions(self):
    for index, card in enumerate(self.dungeon_room.room_slots):
      match card.type:
        case "Monster":
          print(f"[{index+1}] Attack monster {card.format_card()}")
        
        case "Potion":
          print(f"[{index+1}] Use Potion {card.format_card()}")
        
        case "Weapon":
          print(f"[{index+1}] Equip Weapon {card.format_card()}")
          
    self.get_player_answer()
    
  def get_player_answer(self):
    answer = int(input("> "))-1
    #fazer tratamento do input
    
    self.player.interact(self.dungeon_room.room_slots[answer])
    
    
  
  