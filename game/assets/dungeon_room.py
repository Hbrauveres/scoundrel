from constants.constants import MAX_ROOM_SLOTS

class DungeonRoom:
  def __init__(self, deck):
    self.deck = deck
    self.room_slots = []
    self.just_skipped = False
    self.discard_pile = []
    
  def filled_slots(self):
    return len(self.room_slots)  
  
  def draw_room(self):
    if not self.can_draw_room(): return
    
    empty_rooms = MAX_ROOM_SLOTS - self.filled_slots()
    
    for _ in range(empty_rooms):
      self.room_slots.append(self.deck.draw_card())
  
  def skip_room(self):
    cards_on_room = len(self.room_slots)
    
    for _ in range(cards_on_room):
      card = self.room_slots.pop()
      self.deck.place_on_the_bottom(card)
      
    self.just_skipped = True
      
  def can_draw_room(self):
    used_slots = len(self.room_slots)
    
    return used_slots < 4 and used_slots >= 0
  
  def remove_card(self, card):
    if card:
      self.room_slots.remove(card)
  
  def format_room(self):
    formated_room = ""
    
    for card in self.room_slots:
      formated_room += f"[{card.format_card()}] "
      
    return formated_room