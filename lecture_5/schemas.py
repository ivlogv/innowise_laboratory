from pydantic import BaseModel


class BookBase(BaseModel):
    """
    Base model for books.

    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
        year (int | None): Publication year of the book (optional).
    """
    title: str
    author: str
    year: int | None = None


class BookCreate(BookBase):
    """
    Model for creating a book.
    Inherits attributes from BookBase.
    """
    pass


class BookRead(BookBase):
    """
    Model for reading a book.

    Attributes:
        id (int): ID of the book.
    """
    id: int

    class Config:
        # Enable ORM mode to work with ORM objects
        from_attributes = True


class BookDeleteResponse(BaseModel):
    """
    Model for book deletion response.

    Attributes:
        id (int): ID of the deleted book.
        message (str): Deletion status message.
    """
    id: int
    message: str


class BookUpdate(BaseModel):
    """
    Model for updating a book.

    Attributes:
        title (str | None): New title of the book (optional).
        author (str | None): New author of the book (optional).
        year (int | None): New publication year of the book (optional).
    """
    title: str | None = None
    author: str | None = None
    year: int | None = None
