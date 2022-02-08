from random import randint
from player import Player
import random

class Ai(Player): #AI player class

    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        choice = random.randint(0,4)
        self.chosen_gesture = self.list_of_gestures[choice]
