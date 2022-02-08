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
        self.play_round()

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
        if self.player_1.chosen_gesture == self.player_2.chosen_gesture:
            print('TIE')

        elif self.player_1.chosen_gesture == 'Rock' and self.player_2.chosen_gesture == 'Scissors':
            self.player_1.wins += 1
            print(self.player_1.wins)

        elif self.player_1.chosen_gesture == 'Rock' and self.player_2.chosen_gesture == 'Lizard':
            self.player_1.wins += 1
            print(self.player_1.wins)

        elif self.player_1.chosen_gesture == 'Paper' and self.player_2.chosen_gesture == 'Rock':
            self.player_1.wins += 1
            print(self.player_1.wins)
        
        elif self.player_1.chosen_gesture == 'Paper' and self.player_2.chosen_gesture == 'Spock':
            self.player_1.wins += 1
            print(self.player_1.wins)

        elif self.player_1.chosen_gesture == 'Scissors' and self.player_2.chosen_gesture == 'Paper':
            self.player_1.wins += 1
            print(self.player_1.wins)
    
        elif self.player_1.chosen_gesture == 'Scissors' and self.player_2.chosen_gesture == 'Lizard':
            self.player_1.wins += 1
            print(self.player_1.wins)
    
        elif self.player_1.chosen_gesture == 'Lizard' and self.player_2.chosen_gesture == 'Spock':
            self.player_1.wins += 1
            print(self.player_1.wins)

        elif self.player_1.chosen_gesture == 'Lizard' and self.player_2.chosen_gesture == 'Paper':
            self.player_1.wins += 1
            print(self.player_1.wins)
        
        elif self.player_1.chosen_gesture == 'Spock' and self.player_2.chosen_gesture == 'Rock':
            self.player_1.wins += 1
            print(self.player_1.wins)
    
        elif self.player_1.chosen_gesture == 'Spock' and self.player_2.chosen_gesture == 'Scissors':
            self.player_1.wins += 1
            print(self.player_1.wins)
    
        else:
            self.player_2.wins += 1
            print(f'{self.player_2.wins} for player 2')

        
    def play_round(self):
        while self.player_1.wins <= 2 and self.player_2.wins <= 2:  
            
            self.human_show_options()
            self.player_1.choose_gesture()
            self.human_show_options()
            self.player_2.choose_gesture()
            self.compare_player_choices()

    
    
    
    def display_winner(self):
        pass


    def human_show_options(self):
        count = 0
        for gesture in self.player_1.list_of_gestures:
            print(f'{count} to select {gesture}')
            count += 1
