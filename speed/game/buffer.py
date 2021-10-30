import random
from game.actor import Actor
from game.point import Point
from game import constants

class Buffer(Actor):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._text = ' '
        position = Point(1, constants.MAX_Y)
        self.set_position(position)
        self._baseline = "Buffer: "
        self._contents = ""
        self._update_text()
    
    def add_letter(self, letter):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._contents += letter
        self._update_text()

    def _update_text(self):
        self.set_text(self._baseline + " " + self._contents)

    def get_contents(self):
        """
        """
        return self._contents

    def clear(self):
        self._contents = ""
        self._update_text()