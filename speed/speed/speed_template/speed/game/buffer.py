from game.input_service import InputService
from game.word import Word

class Buffer(Word):
    def __init__(self, input_service):
        super().__init__(0,15)
        self.inputs = input_service
        self.keys_pressed = ''
        self.set_word(self.keys_pressed)

    
    #should get inputs and append to key_pressed string
    def get_input(self):
        letter = self.inputs.get_letter()
        self.keys_pressed += letter
        self.set_word(self.keys_pressed)

    def get_buffer_word(self):
        return self.keys_pressed
    
    #Should take the buffer, clear it and send its value
    def clear_buffer(self):
        self.keys_pressed = ''

