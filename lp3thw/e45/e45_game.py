import Labours
import Hero

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        pass

#test_game
print("Welcome to the play test.")
print("What would you name your hero?")
player_name = input("> ")

player = Hero.Hero(player_name)
player.test()