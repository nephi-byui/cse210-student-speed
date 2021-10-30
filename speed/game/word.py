import random
from game.point import Point
from game.constants import MAX_X, MAX_Y

class Word:
    """the user will try to type word. The responsibility of word is to keep track of its string and position. Word will move around randomly if asked to do so.

    Stereotype:
        Information Holder

    Attributes:
        __points (int): The score associated with typing each word.
        __position (Point): The location that each word will appear
    """
    def __init__(self, string) -> None:
        self.word = string 
        self._points = 1
        self._position = Point(random.randint(1, MAX_X -1), random.randint(1, MAX_Y-1) )
        
    def reset(self):
        self._position = Point(random.randint(1, MAX_X-1), random.randint(1, MAX_Y-1) )
  
    def get_points(self):
        return self._points
