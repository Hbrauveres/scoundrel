from constants.constants import *

class Player:
  def __init__(self):
    self.health = MAX_PLAYER_HEALTH
    self.weapon = None
    self.last_defeated = None
    
  def attack(self, card, armed):
    if armed:
      self.health = self.health + self.weapon.effective_value - card.effective_value
      
      self.last_defeated = card
      return 
    
    self.health = self.health - card.effective_value
    
    
  
  def consume(self, card):
    S = self.health + card.effective_value
    M = MAX_PLAYER_HEALTH
    
    self.health = (S + M - abs(S - M)) / 2    
  
  def equip(self, card):
    self.weapon = card
    self.last_defeated = None
  
  def can_attack_with_weapon(self, target):
    if self.last_defeated == None:
      return True
    
    if self.last_defeated.effective_value > target.effective_value:
      return True
    
    return False
  
  def is_alive(self):
    return self.health > 0
  
  def format_player(self):
    player_status = []
    
    player_status.append(f"Health: {self.format_health()}")
    
    if self.weapon:
      player_status.append(f"Current Weapon: {self.weapon.format_card()}")
      
    if self.last_defeated:
      player_status.append(f"Last Defeated: {self.last_defeated.format_card()}")
    
    return "\n".join(player_status)
  
  def format_health(self):
    filled_steps = int(round(MAX_PLAYER_HEALTH * self.health / float(MAX_PLAYER_HEALTH)))
    empty_steps = MAX_PLAYER_HEALTH - filled_steps

    bar = '▮' * filled_steps + '▯' * empty_steps + " "
    return f'{bar} {self.health}/{MAX_PLAYER_HEALTH}'