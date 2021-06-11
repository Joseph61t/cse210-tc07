from game.dictionary import Dictionary
from time import sleep
from game import constants
from game.word import Word
from game.buffer import Buffer

class Director:


    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dict = Dictionary()
        self.words = []
        self._word1 = Word(3)
        self._word1.set_word(self.dict.get_word())
        self.words.append(self._word1)
        self._word2 = Word(5)
        self._word2.set_word(self.dict.get_word())
        self.words.append(self._word2)
        self._word3 = Word(7)
        self._word3.set_word(self.dict.get_word())
        self.words.append(self._word3)
        self._word4 = Word(9)
        self._word4.set_word(self.dict.get_word())
        self.words.append(self._word4)
        self._word5 = Word(11)
        self._word5.set_word(self.dict.get_word())
        self.words.append(self._word5)


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
            for word in self.words:
                if buffer_word == word.word:
                    self._buffer.clear_buffer()
        

                

        if (self._keep_playing == True):
            for word in self.words:
                if word._position.get_x() < 60:
                    word._position = word._position.add(word.get_velocity())
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actors(self.words)       
        self._output_service.flush_buffer()
