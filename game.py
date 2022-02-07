from player import Player

class Game:

    def __init__(self):
        self.player_1 = Player('Name')
        self.player_2 = Player('Name 2')

    def play_game(self):
        self.display_greeting()
        self.how_many_players()
        

    def display_greeting(self):
        print('Hello Gamers.')

    
    
    
    
    
    
    def how_many_players(self):
        player = int(input('Enter amount of players: '))
        
        # if player == 1:
    
    
    
    def compare_player_choices(self):
        pass

    
    
    
    def play_round(self):
        pass

    
    
    
    def display_winner(self):
        pass