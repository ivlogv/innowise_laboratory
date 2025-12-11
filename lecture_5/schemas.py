from pydantic import BaseModel, Field


class BookBase(BaseModel):
    """
    Base model for books.

    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
        year (int | None): Publication year of the book (optional).
    """
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Title of the book",
    )
    author: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Author of the book",
    )
    year: int | None = Field(
        None,
        ge=0,
        le=2025,
        description="Publication year of the book (optional)",
    )


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
    title: str | None = Field(
        None,
        min_length=1,
        max_length=100,
        description="New title of the book",
    )
    author: str | None = Field(
        None,
        min_length=1,
        max_length=100,
        description="New author of the book",
    )
    year: int | None = Field(
        None,
        ge=0,
        le=2025,
        description="New publication year of the book (optional)",
    )
