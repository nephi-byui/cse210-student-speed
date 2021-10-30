from game.actor import Actor

class Explosion(Actor):
    """
    """
    def __init__(self, length):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self.set_text("#" * length)
        self._frames_left = 3

    def flicker(self):
        """
        """
        length = len(self.get_text())
        self._frames_left = self._frames_left - 1
        if self._frames_left == 0:
            self.destroy()
