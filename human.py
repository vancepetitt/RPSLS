from player import Player

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        self.user_name()
    
    def user_name(self):
        self.name = input('Please enter your name: ')

    def choose_gesture(self):
        
        choice = int(input('Please enter choice: '))
           
        correct_input = False
        while correct_input == False:

            if choice == 0 or choice == 1 or choice == 2 or choice == 3 or choice == 4:   
                correct_input = True
                self.chosen_gesture = self.list_of_gestures[choice]
                # print(self.chosen_gesture)

            else:
                choice = int(input('Sorry, unexpected input. Please enter "0", "1", "2", "3", or "4" to select a gesture: '))


