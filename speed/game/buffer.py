# Buffer class to be updated - 
from actor import Actor

class Buffer(Actor):
 
    """
       Handles the buffer

    Stereotype: 
        Service Provider

    Attributes:
        _words: keeps track of the words typed list or inputted
    """
    
    def __init__(self):
        """
        Instantiating COnstructor
        
        Args:
            self (buffer): An instance of buffer.
        """
        super().__init__()
        self._words = []
        self.set_text("Speed-Buffer: ")
        

    def add_word(self, word):
        """
            When word  is a "c" the buffer clears. Otherwise, it adds the a word onto the buffer

        Args:
            self (buffer): An instance of buffer.
            word (str): Inputted words from user
        """

        if word == 'c':
            self._words.clear()
        else:
            self._words.append(word)
        
        self.set_text("".join(self._word))


    def is_word(self, word):
        """
          Transforms the word chaactors list into a string, 
          and compares them to the words on the screen.

        Args:
            self (buffer): An instance of buffer.
            word (str): the word on the screen
        """
        word_to_string = ''.join(self._words)
        if word_to_string.find(word) > -1:
            return True
        else:
            return False
