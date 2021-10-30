class Point:

    def __init__(self, x, y):

        """Represents distance from an origin (0, 0).

        Stereotype:
            Information Holder

        Attributes:
            _x (integer): The horizontal distance.
            _y (Point): The vertical distance.
        """
        self._x = x
        self._y = y

        def get_x(self):

            """Gets the horizontal distance.
        
            Args:
                self (Point): An instance of Point.
                
            Returns:
                integer: The horizontal distance.
            """

            return self._x

        def get_y(self):
            
            """Gets the vertical distance.
        
            Args:
                self (Point): An instance of Point.
                
            Returns:
                integer: The vertical distance.
            """

            return self._y

        def add(self, other):

            """Gets a new point that is the sum of this and the given one.

            Args:
                self (Point): An instance of Point.
                other (Point): The Point to add.

            Returns:
                Point: A new Point that is the sum.
            """

            x = self._x + other.get_x()
            y = self._y + other.get_y()

