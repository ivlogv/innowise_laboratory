from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Book(Base):
    """
    SQLAlchemy model for books.

    Attributes:
        id (int): Primary key ID of the book.
        title (str): Title of the book.
        author (str): Author of the book.
        year (int | None): Publication year of the book (optional).
    """

    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, doc="Primary key ID of the book"
    )
    title: Mapped[str] = mapped_column(
        nullable=False, doc="Title of the book"
    )
    author: Mapped[str] = mapped_column(
        nullable=False, doc="Author of the book"
    )
    year: Mapped[int | None] = mapped_column(
        nullable=True, doc="Publication year of the book (optional)"
    )
