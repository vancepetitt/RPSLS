from unicodedata import name
from player import Player

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        self.user_name()
    
    def user_name(self):
        self.name = input('Please enter your name: ')