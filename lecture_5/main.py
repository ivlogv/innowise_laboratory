from fastapi import FastAPI, Depends, Query, Path
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Annotated

from .database import SessionLocal, init_db, engine
from . import crud, schemas


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager to initialize database on startup."""
    await init_db()
    yield
    # Dispose the engine on shutdown
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to get database session.

    Yields:
        AsyncSession: Async database session.
    """
    async with SessionLocal() as session:
        yield session


DbSession = Annotated[AsyncSession, Depends(get_db)]


@app.get("/")
async def root() -> dict[str, str]:
    """
    Root endpoint to check API status.

    Returns:
        dict[str, str]: Api status.
    """
    return {"status": "ok"}


@app.get("/books/", response_model=list[schemas.BookRead])
async def read_books(db: DbSession) -> list[schemas.BookRead]:
    """
    Get all books from database.

    Args:
        db (AsyncSession): Database session.

    Returns:
        list[BookRead]: List of books.
    """
    return await crud.get_books(db)


@app.get("/books/{book_id}", response_model=schemas.BookRead)
async def read_book(
    book_id: Annotated[
        int,
        Path(gt=0, description="Book ID to retrieve (>0)")
    ],
    db: DbSession
) -> schemas.BookRead:
    """
    Get a book by ID.

    Args:
        book_id (int): ID of the book to retrieve (>0).
        db (AsyncSession): Database session.

    Returns:
        BookRead: The requested book.
    """
    return await crud.get_book(db, book_id)


@app.post("/books/", response_model=schemas.BookRead)
async def create_book(
    book: schemas.BookCreate,
    db: DbSession
) -> schemas.BookRead:
    """
    Create a new book.

    Args:
        book (BookCreate): Book data to create.
        db (AsyncSession): Database session.

    Returns:
        BookRead: The created book.
    """
    return await crud.create_book(db, book)


@app.delete("/books/{book_id}", response_model=schemas.BookDeleteResponse)
async def delete_book(
    book_id: Annotated[int, Path(gt=0, description="Book ID to delete (>0)")],
    db: DbSession
) -> schemas.BookDeleteResponse:
    """
    Delete a book by ID.

    Args:
        book_id (int): ID of the book to delete (>0).
        db (AsyncSession): Database session.

    Returns:
        BookDeleteResponse: The deleted book.
    """
    deleted_book = await crud.delete_book(db, book_id)
    return schemas.BookDeleteResponse(
        id=deleted_book.id,
        message="Book deleted succesfully"
    )


@app.put("/books/{book_id}", response_model=schemas.BookRead)
async def update_book(
    book_id: Annotated[int, Path(gt=0, description="Book ID to update (>0)")],
    book: schemas.BookUpdate,
    db: DbSession
) -> schemas.BookRead:
    """
    Update a book by ID.

    Args:
        book_id (int): ID of the book to update (>0).
        book (BookUpdate): Book data to update.
        db (AsyncSession): Database session.

    Returns:
        BookRead: The updated book.
    """
    return await crud.update_book(db, book_id, book)


@app.get("/books/search/", response_model=list[schemas.BookRead])
async def search_books(
    db: DbSession,
    title: str | None = Query(
        None,
        min_length=1,
        max_length=50
    ),
    author: str | None = Query(
        None,
        min_length=1,
        max_length=50
    ),
    year: int | None = Query(None, ge=0),
) -> list[schemas.BookRead]:
    """
    Search books by title, author or year.

    Args:
        db (AsyncSession): Database session.
        title (str | None): Book title to search.
        author (str | None): Book author to search.
        year (int | None): Book year to search.

    Returns:
        list[BookRead]: List of books that match the search criteria.
    """
    return await crud.search_books(db, title=title, author=author, year=year)
