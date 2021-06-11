from game import constants
from game.actor import Actor
from game.point import Point
from game.dictionary import Dictionary
import random


class Word(Actor):

    def __init__(self):
        super().__init__()
        
        self.word = ""
        velocity = Point(1,0)
        self.set_velocity(velocity)

    def get_word(self):

        return self.word

    def set_word(self, word):
        self.word = word



        

    

        


