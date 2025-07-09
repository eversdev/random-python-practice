class Book:
    """
    Simple Book class with a get method and a str object method, it has one protected attribute

    This class was used for demonstrationale purposes to show that protced instance attributes can
    still be accessed from the outside but it shouldnt as its not recommended and breaks
    encapsulation.
    """

    def __init__(self, name: str, pages: int):
        """
        Initialize object of Book class
        """
        self.name = name
        self._pages = pages

    def get_pages(self):
        """
        Getter method to get the protected instance attribute from within the class
        """
        return self._pages

    # set_pages method??

    def __str__(self) -> str:
        """
        Returns a readable string representation of the Book instance.
        """
        return f"{self.name} is a Book Object"


b1 = Book("Chris", 12)
print(b1)

print(b1.get_pages())


b1._pages = 13

print("-----")

print(b1.get_pages())
