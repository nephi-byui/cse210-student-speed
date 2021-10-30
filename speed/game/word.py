import random
from game import constants
from game.actor import Actor
from game.point import Point
#from game.constants import LIBRARY

class Word(Actor):
    """Words the player is trying to type. The responsibility of Food is to keep track of its string and position. A Food can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder
    Attributes: 
        _points (integer): The number of points the word  is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor.
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self.reset()
    
    def get_points(self):
        """Gets the points the word is worth.
        Args:
            self (Food): an instance of Word.
        Returns:
            integer: The points this food is worth.
        """
        return self._points

    def move_word(self):
        """ Moves the word to the right side of the screen
        Args:
            self (Food): an instance of Food.
        """
        position = self.get_position()
        x = position.get_x() + self._speed
        y = position.get_y()
        self.set_position(Point(x,y))


    def reset(self):
        """Resets the word by moving it to a random position on the left side of the screen.
        Args:
            self (Food): an instance of Food.
        """
        
        # set word
        word_text = random.choice(constants.LIBRARY)
        self.set_text(word_text)

        # random speed
        possible_speeds = range(constants.MIN_WORD_SPEED, constants.MAX_WORD_SPEED)
        self._speed = random.choice(possible_speeds)

        # set position
        x = 1
        y = random.randint(1, constants.MAX_Y - 5)

        position = Point(x, y)

        self.set_position(position)
        #self.set_velocity(Point(0, 0))
        
        # points
        self._points = len(word_text) * self._speed

    def explode(self):
        """ Explodes a word in dramatic fashion
        Args:
            self (Food): an instance of Food.
        """
        length = len(self._text)
        self.set_text("#" * (length + 2))
        self.set_text("+" * (length + 2))
        self.set_text("#" * (length + 2))
        self.reset()
        
