from time import sleep
from game import constants
from game.food import Food
from game.score import Score
from game.buffer import Buffer
import sys

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): Words the player is trying to type.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
     
        self._words = []
        for i in range(0, constants.STARTING_WORDS):
            word = Food()
            word.get_points
            self._words.append(word)

        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the keys the player has typed.

        Args:
            self (Director): An instance of Director.
        """
        self._letter = self._input_service.get_letter()

        #  if player presses Enter
        if self._letter == "*":
            buffer_contents = self._buffer.get_contents()
            self._letter = ''
            self._buffer.clear()
            self._process_buffer(buffer_contents)


    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._buffer.add_letter(self._letter)
        for word in self._words:
            word.move_word()

        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """

        self._output_service.clear_screen()
        self._output_service.draw_actors(self._words)
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._buffer)
        self._output_service.flush_buffer()

    def _process_buffer(self, buffer_contents):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 

        Args:
            self (Director): An instance of Director.
        """
        for word in self._words:
            word_contents = word.get_text()
            if buffer_contents == word_contents:
                points = word.get_points()
                self._score.add_points(points)
                word.explode()
                word.reset()
