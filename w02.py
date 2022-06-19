# W02: Hi-Lo Game Jessica Robertson
import random

class Game:
    # Sets the initial game values
    def __init__(self):
        self.points = Points(300)
        self.firstnum = random.randrange(0, 13)
        self.secondnum = 0
        self.guess = ''
        self.again = ''

    # Displays the initial card value
    def display(self):
        print("The card is: " + str(self.firstnum))
        return self.firstnum

    #Get user input for higer or lower guess
    def hilo(self):
        self.guess = input(f'Higher or lower? [h/l] ')
        self.secondnum = random.randrange(0, 13)
        print("Next card is: " + str(self.secondnum))
        return self.secondnum

    #Calls the points class based on the guess accuracy and card selection
    def change_points(self):
        if self.firstnum >= self.secondnum and self.guess == 'h':
            self.points.decrement(75)
        elif self.firstnum >= self.secondnum and self.guess == 'l':
            self.points.increment(100)
        elif self.firstnum <= self.secondnum and self.guess == 'h':
            self.points.increment(100)
        elif self.firstnum <= self.secondnum and self.guess == 'l':
            self.points.decrement(75)
        else:
            print('Please input an h or an l.')
        print(f'Your score is: ' + str(self.points.getpoints()))

    #Checks if the player wants to play again or ends the game
    def game_over(self):
        while self.points.getpoints() > 0:
            self.again = input('Would you like to play again: [y/n] ')
            if self.again == 'y':
                self.display()
                self.hilo()
                self.change_points()
            else:
                break
        print('Game Over')

class Points:
# Class for modifing points

    #Sets initial point values
    def __init__(self, pointvalue):
        self.points = pointvalue

    #Adds to the point total
    def increment(self, value):
        self.points += value

    #subtracts from the point total
    def decrement(self, value):
        self.points -= value

    #returns point total
    def getpoints(self):
        return self.points

#runs each function needed for game set up
def main():
    game = Game()
    game.display()
    game.hilo()
    game.change_points()
    game.game_over()

main()