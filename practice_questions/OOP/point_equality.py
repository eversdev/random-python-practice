class Point:
    """
    Represents a point in 2D space with x and y coordinates.
    """
    def __init__(self, x, y):
        """
        Initialize a Point instance.

        Parameters:
        x (int or float): The x-coordinate of the point.
        y (int or float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        Compare two Point instances for equality based on their coordinates.

        Parameters:
        other (Point): Another Point instance to compare against.

        Returns:
        bool: True if both points have the same x and y coordinates, False otherwise.
        """
        return self.x == other.x and self.y == other.y



p1 = Point(1,1)
p2 = Point(1,1)
p3 = Point(1,2)

print(p1 == p2)
print(p2 == p3)
