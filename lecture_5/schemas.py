from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str
    year: int | None = None


class BookCreate(BookBase):
    pass


class BookRead(BookBase):
    id: int

    class Config:
        from_attributes = True


class BookDeleteResponse(BaseModel):
    id: int
    message: str


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
