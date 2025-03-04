from game.assets.scoundrel_deck import ScoundrelDeck
from game.assets.dungeon_room import DungeonRoom
from game.assets.player import Player
from game.interaction_menu import InteractionMenu

import os

class Game:
    def __init__(self):
        self.deck = None
        self.player = None
        self.current_turn = 0
        self.dungeon_room = None
        self.interaction_menu = None
        self.is_running = True

    def setup_new_game(self):
        self.deck = ScoundrelDeck()
        self.dungeon_room = DungeonRoom(self.deck)
        self.player = Player()
        self.interaction_menu = InteractionMenu(self.dungeon_room, self.player)

    def run_action_turn(self):
      self.interaction_menu.turn_finished = False
      
      while not self.interaction_menu.turn_finished:
          self.display_game_state()
          action = self.interaction_menu.get_player_action()
          
          if action and self.interaction_menu.confirm_action(action):
            self.process_action(action)
      
      self.current_turn += 1

    def process_action(self, action):
      action.callback()
      self.dungeon_room.remove_card(action.card)
      self.interaction_menu.check_for_auto_end_turn()

    def has_save(self):
        return False

    def display_game_state(self):
        self.clear_terminal()
        
        print(f'--------- Dungeon Room: {self.current_turn} --------')
        print(self.player.format_player())
        print('----------------------------------')
        print(self.dungeon_room.format_room())
        print('----------------------------------')
        print(self.interaction_menu.format_player_options())
        print('----------------------------------')
        
    def clear_terminal(self):
      os.system("cls" if os.name == "nt" else "clear")