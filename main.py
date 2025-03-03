from engine.engine import Engine
from game.game import Game

def main():
  engine = Engine()
  game = Game()
  engine.start(game)
  
if __name__ == "__main__":
  main()