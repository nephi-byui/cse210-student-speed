import random
from game import constants
from game.actor import Actor
from game.point import Point

class Food(Actor):
    """Words the player is trying to type. The responsibility of Food is to keep track of its string and position. A Food can move around randomly if asked to do so. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self.set_text("")
        self.reset()
    
    def get_points(self):
        """Gets the points this food is worth.
        Args:
            self (Food): an instance of Food.
        Returns:
            integer: The points this food is worth.
        """
        return self._points

    def move_word(self):
        """ Launches the word in the given direction
        """
        position = self.get_position()
        x = position.get_x() + self._speed
        y = position.get_y()
        self.set_position(Point(x,y))


    def reset(self):
        """Resets the food by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.
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
        
        # points
        self._points = len(word_text) * self._speed

    def explode(self):
        """ Explodes a word in dramatic fashion
        """
        length = len(self._text)
        self.set_text("#" * (length + 2))
        self.set_text("+" * (length + 2))
        self.set_text("#" * (length + 2))
        self.reset()
        
