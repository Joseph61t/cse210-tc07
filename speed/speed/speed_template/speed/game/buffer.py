from input_service import InputService


class Buffer:
    def __init__(self, input_service):
        
        self.inputs = input_service
        self.keys_pressed = ''
    
    #should get inputs and append to key_pressed string
    def get_input(self):
        letter = self.inputs.get_letter()
        self.keys_pressed + letter
    
    #Should take the buffer, clear it and send its value
    def clear_buffer(self):
        word = self.keys_pressed
        self.keys_pressed = ''
        return word

