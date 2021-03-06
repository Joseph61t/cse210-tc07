from game.actor import Actor
from game.dictionary import Dictionary
from time import sleep
from game import constants
from game.word import Word
from game.buffer import Buffer
from game.point import Point

class Director:


    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dict = Dictionary()
        self.words = []
        self._word1 = Word(0,3)
        self._word1.set_word(self.dict.get_word())
        self.words.append(self._word1)
        self._word2 = Word(0,5)
        self._word2.set_word(self.dict.get_word())
        self.words.append(self._word2)
        self._word3 = Word(0,7)
        self._word3.set_word(self.dict.get_word())
        self.words.append(self._word3)
        self._word4 = Word(0,9)
        self._word4.set_word(self.dict.get_word())
        self.words.append(self._word4)
        self._word5 = Word(0,11)
        self._word5.set_word(self.dict.get_word())
        self.words.append(self._word5)

        self.score = Word(0,1)
        self.score.set_word(0)

        self._input_service = input_service
        self._buffer = Buffer(self._input_service)
        self._keep_playing = True
        self._output_service = output_service
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        self._buffer.get_input()
        
        



    def _do_updates(self):
        buffer_word = self._buffer.get_buffer_word()


        if '\r' in buffer_word:
            self._buffer.clear_buffer()
            buffer_word = buffer_word.strip('\r')
            #Checks if the words match
            for curr_word in self.words:
                if buffer_word == curr_word.word:
                    self.score.set_word(self.score.get_word() + len(curr_word.word))
                    curr_word.reset_word(self.dict.get_word(), Point(0, curr_word._position.get_y()))
        

                

        if (self._keep_playing == True):
            for curr_word in self.words:
                if curr_word._position.get_x() < 60:
                    curr_word._position = curr_word._position.add(curr_word.get_velocity())
                else:
                    curr_word.reset_word(self.dict.get_word(), Point(0, curr_word._position.get_y()))

    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self.words)
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actor(self.score)       
        self._output_service.flush_buffer()
