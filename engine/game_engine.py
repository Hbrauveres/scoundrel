from assets.scoundrel_deck import ScoundrelDeck
from assets.dungeon_room import DungeonRoom
from assets.player import Player
from engine.interaction_menu import InteractionMenu

class Engine:
    _instance = None
  
    def __new__(cls):
      if cls._instance is None:
        cls._instance = super().__new__(cls)
      return cls._instance
    
    def __init__(self):
      self.deck = None
      self.player = None
      self.current_turn = 0
      self.dungeon_room = None
    
    def setup_new_game(self):
      self.deck = ScoundrelDeck()
      self.dungeon_room = DungeonRoom(self.deck)
      self.player = Player()
      self.interaction_menu = InteractionMenu(self.dungeon_room, self.player)
      
    def has_save(self):
      return False
      
    def start(self):
      if self.has_save():
        return
      
      self.setup_new_game()
      self.game_loop()
      
    def game_loop(self):
      while(self.player.is_alive()):
        self.dungeon_room.draw_room()
        # do game stuff
        self.draw_game_state()
      
    def draw_game_state(self):
        print('----------------------------------')
        print(self.player.format_player())
        print('----------------------------------')
        print(self.dungeon_room.format_room())
        print('----------------------------------')
        self.interaction_menu.DisplayPlayerOptions()
      