from speed.speed.speed_template.speed.game.dictionary import Dictionary
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
        self._word1 = Word()
        self._word2 = Word()
        self._word3 = Word()
        self._word4 = Word()
        self._word5 = Word()

        self.dict = Dictionary()

        self._buffer = Buffer()

        self._input_service = input_service
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
        letter = self._buffer.get_input()

        "Checks the letter in word" 
        for letter in Word:
            for letter in Buffer:
                if (letter == Buffer):
                    break


    def _do_updates(self):
        if (self._keep_playing == True):
            self._word1.point.add()
            self._word2.point.add()
            self._word3.point.add()
            self._word4.point.add()
            self._word5.point.add()
        
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
