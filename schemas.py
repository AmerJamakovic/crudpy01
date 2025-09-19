from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
import datetime


# -----USER SCHEMAS----
class UserBase(BaseModel):
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserReadSimple(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserRead(UserBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True


# -----MOVIE SCHEMAS-----
class MovieBase(BaseModel):
    title: str
    release_date: datetime.date
    rating: Optional[float] = None


class MovieCreate(MovieBase):
    pass


class MovieReadSimple(MovieBase):
    id: int
    title: str

    class Config:
        orm_mode = True


class MovieRead(MovieBase):
    id: int

    categories: Optional[List["CategoryReadSimple"]] = []

    class Config:
        orm_mode = True


# -----CATEGORY SCHEMAS-----
class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryReadSimple(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class CategoryRead(CategoryBase):
    id: int
    movies: Optional[List[MovieRead]] = []

    class Config:
        orm_mode = True


# -----RENTAL SCHEMAS-----
class RentalBase(BaseModel):
    rental_date: datetime.date
    return_date: Optional[datetime.date] = None


class RentalCreate(RentalBase):
    user_id: int
    movie_id: int


class RentalRead(RentalBase):
    id: int
    user: UserReadSimple
    movie: MovieReadSimple

    class Config:
        orm_mode = True


MovieRead.update_forward_refs()
CategoryRead.update_forward_refs()
