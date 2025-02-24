class MenuOption:
    def __init__(self, option_num, card):
        self.option_num = option_num
        self.card = card
        
    def format_action_message(self):
        match self.type:
            case "Monster":
                return f"[{self.option_num}] Attack Monster {self.card.format_card()}"
            
            case "Potion":
                return f""
            
            case "Weapon":
                return f""