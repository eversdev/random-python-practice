class Book:
    """
    Simple Book class representing a book with a title and an author.
    Contains a dunder method that overrides the default string representation.
    """

    def __init__(self, title, author, pages) -> None:
        """
        Initialize a Book instance with a title, author, and page count.
        """
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        """
        Return a user-friendly string showing the book's title and author.
        Overrides the default __str__ method.
        """
        return f"{self.title} by {self.author}"

    def __len__(self) -> int:
        """
        Return the number of pages when len(book) is called.
        """
        return self.pages

    def __repr__(self):
        return f"Book('{self.title}','{self.author}',{self.pages})"


b1 = Book("The Shining", "Stephen King", 356)
print(b1)


print(len(b1))
print(repr(b1))
