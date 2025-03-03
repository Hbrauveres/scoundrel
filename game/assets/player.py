from constants.constants import *

class Player:
  def __init__(self):
    self.health = MAX_PLAYER_HEALTH
    self.weapon = None
    
  def attack(self, card, armed):
    if armed:
      self.health = self.health + self.weapon.effective_value - card.effective_value
      return 
    
    self.health = self.health - card.effective_value
  
  def consume(self, card):
    S = self.health + card.effective_value
    M = MAX_PLAYER_HEALTH
    
    self.health = (S + M - abs(S - M)) / 2    
  
  def equip(self, card):
    self.weapon = card
  
  def is_alive(self):
    return self.health > 0
  
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