class Player:
    
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.chosen_gesture = ''
        self.list_of_gestures = []
        self.create_gestures()
    
    
    def create_gestures(self):

        gesture_one = 'Rock'
        gesture_two = 'Scissors'
        gesture_three = 'Paper'
        gesture_four = 'Lizard'
        gesture_five = 'Spock'

        self.list_of_gestures.append(gesture_one)
        self.list_of_gestures.append(gesture_two)
        self.list_of_gestures.append(gesture_three)
        self.list_of_gestures.append(gesture_four)
        self.list_of_gestures.append(gesture_five)

    
    
    
    # def choose_gesture(self):
    #     pass

    