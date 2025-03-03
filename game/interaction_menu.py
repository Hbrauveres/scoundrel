from constants import constants
from game.menu_option import MenuOption

class InteractionMenu:
  def __init__(self, dungeon_room, player):
    self.dungeon_room = dungeon_room
    self.player = player
    self.selected_card = None
    self.menu_options = {}
    self.qty_menu_options = 0
    self.turn_finished = False
  
  def confirm_action(self, action):
    choice = input(f"Confirm: [{action.text}] y/n\n> ")
    
    if choice == 'y':
      return True
    
    return False
    
  
  def format_player_options(self):
    self.clear_menu_options()
    self.set_menu_options()
    
    action_options = []
    
    for num, option in self.menu_options.items():
      action_options.append(f"{option.format_option_text()}") 
    
    return "\n".join(action_options)
  
  def set_menu_options(self):
    callback_fn = None
    
    for index, card in enumerate(self.dungeon_room.room_slots):
      match card.type:
        case constants.MONSTER:
          callback_fn = self.handle_attack
          
        case constants.POTION:
          callback_fn = self.handle_potion
          
        case constants.WEAPON:
          callback_fn = self.handle_equip

      self.menu_options[index+1] = MenuOption(index+1, card.action_text + " " + card.format_card(), callback_fn)
      
    if self.dungeon_room.can_skip and self.dungeon_room.filled_slots() == 4:
      self.menu_options[len(self.menu_options)+1] = MenuOption(len(self.menu_options)+1, "Skip room (Send all cards to deck's bottom)", self.handle_skip_room)
    
    if self.dungeon_room.filled_slots() < 4:
      self.menu_options[len(self.menu_options)+1] = MenuOption(len(self.menu_options)+1, "End Turn", self.handle_end_turn)
  
  def clear_menu_options(self):
    self.menu_options = {}
    self.selected_card = None
  
  def get_player_action(self):
    user_input = int(input("> "))
    
    if user_input in self.menu_options.keys():
      return self.menu_options[user_input]
    
    print("Invalid option")
    return None
    
  def handle_attack(self):
    print('----------------------------------')
    
    if not self.player.weapon:
      self.player.attack(self.selected_card, choice)
      
      return
      
    choice = input("Do you want to use your weapon? y/n\n> ")
    
    if choice.lower() in ("y", "n"):
        self.player.attack(self.selected_card, choice)
    else:
        print("Opção de ataque inválida!")

  def handle_equip(self):
    self.player.equip_weapon(self.selected_card)

  def handle_potion(self):
    self.player.heal(self.selected_card)
          
  def handle_skip_room(self):
    pass
  
  def handle_end_turn(self):
    self.turn_finished = True