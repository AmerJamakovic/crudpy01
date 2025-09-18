from typing import List, Optional
from sqlalchemy import Column, BigInteger, String, Date, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)


    rentals: Mapped[List["Rental"]] = relationship("Rental", back_populates="user")



class Rental(Base):
    __tablename__ = "rentals"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id"), nullable=False)
    movie_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("movies.id"), nullable=False)
    rental_date: Mapped[Date] = mapped_column(Date, nullable=False)
    return_date: Mapped[Optional[Date]] = mapped_column(Date, nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="rentals")
    movie: Mapped["Movie"] = relationship("Movie", back_populates="rentals")



class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    movies_title: Mapped[str] = mapped_column(String, nullable=False)
    release_date: Mapped[Date] = mapped_column(Date, nullable=False)
    rating: Mapped[Optional[float]] = mapped_column(Float, nullable=True)

    rentals: Mapped[List["Rental"]] = relationship("Rental", back_populates="movie")

    categories: Mapped[List["Category"]] = relationship(
        "Category",
        secondary="movies_categories",
        back_populates="movies"
    )



class MovieCategory(Base):
    __tablename__ = "movies_categories"

    movie_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("movies.id"), primary_key=True)
    category_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("categories.id"), primary_key=True)


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    category_name: Mapped[str] = mapped_column(String, nullable=False)

    movies: Mapped[List["Movie"]] = relationship(
        "Movie",
        secondary="movies_categories",
        back_populates="categories"
    )
