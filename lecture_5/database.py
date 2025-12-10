from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncEngine,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase

# Database URL for SQLite database
DATABASE_URL = "sqlite+aiosqlite:///./lecture_5/books.db"


# Create async engine and session maker
engine: AsyncEngine = create_async_engine(url=DATABASE_URL, echo=True)
SessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class Base(DeclarativeBase):
    """Base class for declarative models."""
    pass


async def init_db() -> None:
    """Initialize the database by creating all tables."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
