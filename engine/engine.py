class Engine:
    def start(self, game):
        if game.has_save():
            # Carregar jogo salvo se houver
            pass
        else:
            game.setup_new_game()
    
        self.game_loop(game)
        
    def game_loop(self, game):
        while game.is_running:
            game.dungeon_room.draw_room()
            game.run_action_turn()