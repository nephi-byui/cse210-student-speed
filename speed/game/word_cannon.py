from constants import *
from word import Word
import random

class WordCannon:
    """
    """
    def __init__(self) -> None:
        self.library = LIBRARY

    def shoot_word(self):
        """
        returns a Word() object
        """
        word = Word(random.choice(self.library))
        return word

    