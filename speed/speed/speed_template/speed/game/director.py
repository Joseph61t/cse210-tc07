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
        self.words = []
        self._word1 = Word()
        self.words.append(self._word1)
        self._word2 = Word()
        self.words.append(self._word2)
        self._word3 = Word()
        self.words.append(self._word3)
        self._word4 = Word()
        self.words.append(self._word4)
        self._word5 = Word()
        self.words.append(self._word5)

        self.dict = Dictionary()

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
        buffer_word = self._buffer.get_input()

        #Checks if the words match
        for word in self.words:
            if buffer_word == word:
                # TODO add points, delete, and create new word!
                pass
        



    def _do_updates(self):
        if (self._keep_playing == True):
            for word in self.words:
                word.position.add(word.get_velocity())
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._word1)       
        self._output_service.draw_actor(self._word2)
        self._output_service.draw_actor(self._word3)
        self._output_service.draw_actor(self._word4)
        self._output_service.draw_actor(self._word5)
        self._output_service.flush_buffer()
