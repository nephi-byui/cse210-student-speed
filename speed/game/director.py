from game.hud import Hud

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

        self.hud = Hud

    def start_game(self):
        print('pass')

    def handle_word_entered():
        """ Handles the event of the user pressing Enter
        """

        
    