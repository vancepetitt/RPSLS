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
        print_slow('Hello Gamers \n Welcome to Rock, Paper, Scissors, Lizard, Spock. (RPSLS)\n')
        print_slow('The game is best 2 out of 3 \n ')
        print_slow('The rules, as stated by Sheldon from "The Big Bang Theory":\n"Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard,\nLizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard,\nLizard eats Paper, Paper disproves Spock, Spock vaporizes rock,\nand as it always has, Rock crushes Scissors.\n"')

    
    
    
    
    
    
    def how_many_players(self):

        player = input('Enter number of players: ')
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
        
        while self.player_1.wins < 2 and self.player_2.wins < 2:  
            
            self.human_show_options()
            self.player_1.choose_gesture()
            self.human_show_options()
            self.player_2.choose_gesture()
            self.compare_player_choices()

        self.display_winner()

    
    
    
    def display_winner(self):
        
        if self.player_1.wins == 2:
            print(f'{self.player_1.name} wins!')
        else:
            print(f'{self.player_2.name} wins!')


    def human_show_options(self):
        count = 0
        for gesture in self.player_1.list_of_gestures:
            print(f'{count} to select {gesture}')
            count += 1

    