from constants.constants import MAX_ROOM_SLOTS

class DungeonRoom:
  def __init__(self, deck):
    self.deck = deck
    self.room_slots = []
    self.used_slots = len(self.room_slots)
    
  def draw_room(self):
    if not self.can_draw_room(): return
    
    empty_rooms = MAX_ROOM_SLOTS - self.used_slots
    
    for _ in range(empty_rooms):
      self.room_slots.append(self.deck.draw_card())
    
  
  def skip_room(self):
    for _ in self.room_slots:
      card = self.room_slots.pop()
      
      self.deck.place_on_the_bottom(card)
      
  def can_draw_room(self):
    used_slots = len(self.room_slots)
    
    return used_slots < 4 and used_slots >= 0
  
  def format_room(self):
    formated_room = ""
    
    for card in self.room_slots:
      formated_room += f"[{card.format_card()}] "
      
    return formated_room