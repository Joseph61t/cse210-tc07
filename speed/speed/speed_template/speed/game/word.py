from game import constants
from game.actor import Actor
from game.point import Point
from game.dictionary import Dictionary
import random


class Word(Actor):

    def __init__(self):

        super().__init__()
        self.word = ""
        velocity = Point(3,0)
        self.set_velocity(velocity)

    def get_word(self):

<<<<<<< HEAD
        self.velocity = random.randint(1,10)
=======
        return self.word
>>>>>>> 2e4c1c00bba281b16b5110a269242ac11f8784a0

    def set_word(self, word):
        self.word = word



        

    

        


