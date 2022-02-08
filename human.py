from player import Player

class Human(Player):

    def __init__(self, name):
        super().__init__(name)
        self.user_name()
    
    def user_name(self):
        self.name = input('Please enter your name: ')

    def choose_gesture(self):
        choice = int(input('Please enter choice: '))
        self.chosen_gesture = self.list_of_gestures[choice]
        print(self.chosen_gesture)


