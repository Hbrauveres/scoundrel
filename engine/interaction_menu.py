from engine.menu_option import MenuOption


class InteractionMenu:
  def __init__(self, dungeon_room, player):
    self.dungeon_room = dungeon_room
    self.player = player
    self.menu_options = []
  
  def attack_dialog_callback(self, card):
    pass
  
  def use_potion_dialog_callback(self, card):
    pass
  
  def confirm_dialog_callback(self, card):
    pass
  
  def display_player_options(self):
    self.reset_menu_options()
    
    for index, card in enumerate(self.dungeon_room.room_slots):
      self.menu_options.append(MenuOption(index+1, card))
          
    self.get_player_answer()
  
  def reset_menu_options(self):
    self.menu_options = []
  
  def get_player_answer(self):
    answer = int(input("> "))-1
    #fazer tratamento do input
    
    self.player.interact(self.dungeon_room.room_slots[answer])
    
    
  
  