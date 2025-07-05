class Book:
    """
    Simple Book class representing a book with a title and an author.
    Contains a dunder method that overrides the default string representation.
    """
    def __init__(self, title, author) -> None:
        """
         Initialize a Book instance with a title and an author.
        """
        self.title = title
        self.author = author
    
    def __str__(self) -> str:
        """
        Return a user-friendly string showing the book's title and author.
        Overrides the default __str__ method.
        """
        return f"{self.title} by {self.author}"
    


b1 = Book("The Shining", "Stephen King" )

print(b1)


