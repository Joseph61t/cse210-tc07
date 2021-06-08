import random
from typing import Text

class Dictionary:

    def __init__(self):
        self._words = []
        self.load_words()
        
    # reads the file and adds it to a list, to be only called in the constrcutor  
    # for some reason the method doens't recognize the words.txt file right now
    # so it doesn't work   
    def load_words(self):
        
        with open("speed\speed\speed_template\speed\game\dict.txt") as file:
            for line in file:
                self._words.append(line)
            print('done loading words')

    # returns a random word from the list
    def get_word(self):
        return self._words[random.randint(0,9885)]




# dictionary = Dictionary()
# print(dictionary.get_word())
