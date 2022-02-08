from ai import Ai
from human import Human
from player import Player
import sys, time, random

def print_slow(str): #Function in order for text to print slowly
        for letter in str:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.05)



class Game:

    def __init__(self):
        self.player_1 = Player('Name 1')
        self.player_2 = Player('Name 2')

    def play_game(self):
        self.display_greeting()
        self.how_many_players()
        self.play_round()

    def display_greeting(self):
        print_slow('Hello Gamers\n\nWelcome to Rock, Paper, Scissors, Lizard, Spock. (RPSLS)\n\n')
        print_slow('The game is best 2 out of 3\n\n')
        print_slow('The rules, as stated by Sheldon from "The Big Bang Theory":\n"Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard,\nLizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,\nLizard eats Paper, Paper disproves Spock, Spock vaporizes rock,\nand as it always has, Rock crushes Scissors."\n\n')

    
    
    
    
    
    
    def how_many_players(self):

        player = input('\nEnter number of players: ')
        correct_input = False
        while correct_input == False:

            if player == '1':
                correct_input = True
                self.player_1 = Human('')
                self.player_2 = Ai('Computer')
        
            elif player == '2':
                correct_input = True
                self.player_1 = Human('')
                print('Alright, Player Two')
                self.player_2 = Human('Player 2')

            else:
                player = input('Sorry, only one or two players can play the game. Please enter "1" or "2": ')

    
    def compare_player_choices(self):
        if self.player_1.chosen_gesture == self.player_2.chosen_gesture:
            print('TIE')

        elif self.player_1.chosen_gesture == 'Rock' and self.player_2.chosen_gesture == 'Scissors':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')

        elif self.player_1.chosen_gesture == 'Rock' and self.player_2.chosen_gesture == 'Lizard':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')

        elif self.player_1.chosen_gesture == 'Paper' and self.player_2.chosen_gesture == 'Rock':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')
        
        elif self.player_1.chosen_gesture == 'Paper' and self.player_2.chosen_gesture == 'Spock':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')

        elif self.player_1.chosen_gesture == 'Scissors' and self.player_2.chosen_gesture == 'Paper':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')
    
        elif self.player_1.chosen_gesture == 'Scissors' and self.player_2.chosen_gesture == 'Lizard':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')
    
        elif self.player_1.chosen_gesture == 'Lizard' and self.player_2.chosen_gesture == 'Spock':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')

        elif self.player_1.chosen_gesture == 'Lizard' and self.player_2.chosen_gesture == 'Paper':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')
        
        elif self.player_1.chosen_gesture == 'Spock' and self.player_2.chosen_gesture == 'Rock':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')
    
        elif self.player_1.chosen_gesture == 'Spock' and self.player_2.chosen_gesture == 'Scissors':
            self.player_1.wins += 1
            print(f'{self.player_1.wins} win for {self.player_1.name}!')
    
        else:
            self.player_2.wins += 1
            print(f'{self.player_2.wins} win for {self.player_2.name}!')

        
    def play_round(self):
        
        round = 1

        while self.player_1.wins < 2 and self.player_2.wins < 2:  
            
            input('Press enter to start next round.')
            print(f'\n\n*ROUND {round}*')
            print_slow(f'{self.player_1.name}:\n')
            self.human_show_options()
            self.player_1.choose_gesture()
            print_slow(f'{self.player_2.name}:\n')
            self.human_show_options()
            self.player_2.choose_gesture()
            print_slow('3..2..1..Shoot!\n')
            print(f'{self.player_1.name} plays {self.player_1.chosen_gesture}! {self.player_2.name} plays {self.player_2.chosen_gesture}!')
            self.compare_player_choices()
            round += 1

        self.display_winner()

    
    
    
    def display_winner(self):
        
        if self.player_1.wins == 2:
            print(f'\n{self.player_1.name} wins!')
        else:
            print(f'\n{self.player_2.name} wins!')


    def human_show_options(self):
        count = 0
        for gesture in self.player_1.list_of_gestures:
            print(f'{count} to select {gesture}')
            count += 1

    