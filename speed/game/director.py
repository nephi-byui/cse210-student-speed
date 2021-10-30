from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _words (list)                   : a list of Word(Actor) objects
        _input_service (InputService)   : The input mechanism
        output_service (OutputService)  : the output mechanism

        _keep_playing (boolean)         : continue playing while True
        _score (Score)                  : an instance of Score(Actor)
        _buffer (Buffer)                : an instance of Buffer(Actor)

        _letter (STR)                   : a letter
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
       
        self._words = []
        for i in range(0, constants.STARTING_WORDS):
            word = Word()
            word.get_points
            self._words.append(word)

        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        #self._snake = Snake()
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
        """Gets the inputs at the beginning of each round of play.
            > gets the letter from input service
            > updates the buffer if user presses Enter
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

    def _process_buffer(self, buffer_contents):
        for word in self._words:
            word_contents = word.get_text()
            if buffer_contents == word_contents:
                points = word.get_points()
                self._score.add_points(points)
                word.explode()
                word.reset()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._buffer.add_letter(self._letter)

        # move words and reset words that hit the right side
        
        for word in self._words:
            word.move_word()
        
        for word in self._words:
            position = word.get_position()
            x = position.get_x()
            if x >= constants.MAX_X:
                word.reset()
        
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

