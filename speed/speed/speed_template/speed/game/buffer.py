from speed.speed.speed_template.speed.game.actor import Actor
from game.input_service import InputService
from game.actor import Actor

class Buffer(Actor):
    def __init__(self, input_service):
        self.set_position(0, 15)
        self.inputs = input_service
        self.keys_pressed = ''
        self.set_text(self.keys_pressed)

    
    #should get inputs and append to key_pressed string
    def get_input(self):
        letter = self.inputs.get_letter()
        self.keys_pressed += letter

    def get_buffer_word(self):
        return self.keys_pressed
    
    #Should take the buffer, clear it and send its value
    def clear_buffer(self):
        self.keys_pressed = ''

