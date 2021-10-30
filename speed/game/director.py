from time import sleep
from game.hud import Hud
from game import constants
from game import input_service

class Director:
    """ Responsible for the flow of gameplay
    """
    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._keep_playing = True
        self._input_service = input_service
        self._output_service = output_service

        self.buffer = ""
        self.hud = Hud()

    def start_game(self):
        self._output_service._screen.print_at('red', 5, 7, colour=7, attr=0, bg=0, transparent=False)
        while self._keep_playing:
            self._output_service._screen.print_at('red', 5, 7, colour=7, attr=0, bg=0, transparent=False)
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play.
        Get the buffer

        Args:
            self (Director): An instance of Director.
        """
        letter = self._input_service.get_letter()
        self.buffer += letter
        
    def _do_updates(self):
        """Updates the important game information for each round of play.
        
        In this case, that means redrawing the actors, and the score and buffer updating
        Args:
            self (Director): An instance of Director.
        """
        # update buffer

        # draw actors
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        pass
    """
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._food)
        self._output_service.draw_actors(self._snake.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()"""