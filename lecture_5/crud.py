from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from .models import Book
from .schemas import BookCreate, BookUpdate


async def get_books(session: AsyncSession):
    result = await session.execute(select(Book))
    return result.scalars().all()


async def get_book(session: AsyncSession, id: int):
    result = await session.execute(select(Book).where(Book.id == id))
    return result.scalar()


async def create_book(session: AsyncSession, book: BookCreate):
    new_book = Book(title=book.title, author=book.author, year=book.year)
    session.add(new_book)
    await session.commit()
    await session.refresh(new_book)
    return new_book


async def delete_book(session: AsyncSession, id: int):
    result = await session.execute(select(Book).filter(Book.id == id))
    book = result.scalar_one_or_none()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    await session.delete(book)
    await session.commit()
    return book


async def update_book(
    session: AsyncSession,
    id: int, data: BookUpdate
):
    result = await session.execute(select(Book).filter(Book.id == id))
    book = result.scalar_one_or_none()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    if data.title is not None:
        book.title = data.title
    if data.author is not None:
        book.author = data.author
    if data.year is not None:
        book.year = data.year

    await session.commit()
    await session.refresh(book)
    return book


async def search_books(
    session: AsyncSession,
    title: str | None = None,
    author: str | None = None,
    year: int | None = None
):
    stmt = select(Book)

    if title:
        stmt = stmt.filter(Book.title.ilike(f"%{title}%"))
    if author:
        stmt = stmt.filter(Book.author.ilike(f"%{author}%"))
    if year is not None:
        stmt = stmt.filter(Book.year == year)

    result = await session.execute(stmt)
    return result.scalars().all()
