from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):

    def __init__(self):

        super().__init__()

    def velocity(self):

        self.velocity = randint(1,10)


    def text(self):


