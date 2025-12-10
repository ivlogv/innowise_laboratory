from fastapi import FastAPI, Depends, Query, Path
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Annotated

from .database import SessionLocal, init_db
from . import crud, schemas


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


DbSession = Annotated[AsyncSession, Depends(get_db)]


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/books/", response_model=list[schemas.BookRead])
async def read_books(db: DbSession):
    return await crud.get_books(db)


@app.get("/books/{book_id}", response_model=schemas.BookRead)
async def read_book(
    book_id: Annotated[int, Path(gt=0, description="Book ID to retrieve >0")],
    db: DbSession
):
    return await crud.get_book(db, book_id)


@app.post("/books/", response_model=schemas.BookCreate)
async def create_book(
    book: schemas.BookCreate,
    db: DbSession
):
    return await crud.create_book(db, book)


@app.delete("/books/{book_id}", response_model=schemas.BookDeleteResponse)
async def delete_book(
    book_id: Annotated[int, Path(gt=0, description="Book ID to delete >0")],
    db: DbSession
) -> schemas.BookDeleteResponse:
    deleted_book = await crud.delete_book(db, book_id)
    return schemas.BookDeleteResponse(
        id=deleted_book.id,
        message="Book deleted succesfully"
    )


@app.put("/books/{book_id}", response_model=schemas.BookRead)
async def update_book(
    book_id: Annotated[int, Path(gt=0, description="Book ID to update >0")],
    book: schemas.BookUpdate,
    db: DbSession
):
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
):
    return await crud.search_books(db, title=title, author=author, year=year)
