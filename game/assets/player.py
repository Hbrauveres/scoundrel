from constants.constants import *

class Player:
  def __init__(self):
    self.health = MAX_PLAYER_HEALTH
    self.weapon = None
    
  def attack(self, card, armed):
    pass
  
  def consume(self, card):
    pass
  
  def equip(self, card):
    pass
      
  def lose_health(self, value):
    pass
  
  def gain_health(self, value):
    pass
  
  def is_alive(self):
    return self.health >= MAX_PLAYER_HEALTH
  
  def format_player(self):
    player_status = f"Health: {self.format_health()}\nCurrent Weapon: "
    
    if self.weapon:
      player_status += f"{self.weapon.format_card()}"
      
      return player_status
    
    return player_status
  
  def format_health(self):
    filled_steps = int(round(MAX_PLAYER_HEALTH * self.health / float(MAX_PLAYER_HEALTH)))
    empty_steps = MAX_PLAYER_HEALTH - filled_steps

    bar = '▮' * filled_steps + '▯' * empty_steps + " "
    return f'{bar} {self.health}/{MAX_PLAYER_HEALTH}'