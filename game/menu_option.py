class MenuOption:
  def __init__(self, option_num, text, card, callback):
    self.option_num = option_num
    self.card = card
    self.text = text
    self.callback = callback
    
    
  def format_option_text(self):
    return f"[{self.option_num}] {self.text}"
  