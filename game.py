from ai import Ai
from human import Human
from player import Player

class Game:

    def __init__(self):
        self.player_1 = Human('Name')
        self.player_2 = Player('Name 2')

    def play_game(self):
        self.display_greeting()
        self.how_many_players()
        

    def display_greeting(self):
        print('Hello Gamers.')

    
    
    
    
    
    
    def how_many_players(self):
        player = int(input('Enter amount of players: '))

        if player == 1:
            self.player_2 = Ai('Computer')
        
        
        if player == 2:
            print('Alright, Player Two')
            self.player_2 = Human('Player 2')
        
        print(self.player_1.name)

        print(self.player_2.name)

    
    
    
    def compare_player_choices(self):
        pass

    
    
    
    def play_round(self):
        pass

    
    
    
    def display_winner(self):
        pass