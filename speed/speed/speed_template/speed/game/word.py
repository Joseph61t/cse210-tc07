from game import constants
from game.actor import Actor
from game.point import Point
from game.dictionary import Dictionary
import random


class Word(Actor):

    def __init__(self, x, y):
        super().__init__()
        position = Point(x, y)
        self.set_position(position)
        self.word = ""
        velocity = Point(1,0)
        self.set_velocity(velocity)

    def get_word(self):

        return self.word

    def set_word(self, word):
        self.word = word

    def reset_word(self, new_word, new_position):
        self.set_word(new_word)
        self.set_position(new_position)


        

    

        


