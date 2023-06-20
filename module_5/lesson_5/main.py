# pip install sqlalchemy
import datetime
from typing import List

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime, func, Table
# create_engine("postgres://user:pass@localhost/database")
from sqlalchemy.orm import declarative_base, mapped_column, Mapped, relationship, sessionmaker

engine = create_engine("postgresql://postgres:1@localhost:5432/postgres")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()
# #
# # class User(Base):
# #     __tablename__ = "users"
# #     id: Mapped[int] = mapped_column(primary_key=True)
# #     name : Mapped[str] = mapped_column(String(255))
# #     posts: Mapped[List["Post"]] = relationship("Post" , back_populates='user')
# #
# #     def __repr__(self):
# #         return f"{self.name}"
# #
# # class Post(Base):
# #     __tablename__ = "posts"
# #     id: Mapped[int] = mapped_column(primary_key=True)
# #     user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
# #     title : Mapped[str] = mapped_column(String(255) , nullable=True)
# #     description: Mapped[str] = mapped_column(Text)
# #     user : Mapped["User"] = relationship("User", back_populates="posts")
# #
# #     def __repr__(self):
# #         return self.title
# class Language(Base):
#     __tablename__ = "language"
#
#     # language_id = mapped_column(Integer , primary_key=True)
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name : Mapped[str] = mapped_column(String(10))
#     last_update: Mapped[str] = mapped_column(default=datetime.datetime.utcnow)
#     films : Mapped[List["Film"]] = relationship(back_populates="language")
#     def __repr__(self):
#         return self.name
#
# class Film(Base):
#     __tablename__ = "film"
#
#     # language_id = mapped_column(Integer , primary_key=True)
#     film_id: Mapped[int] = mapped_column(primary_key=True)
#     language_id: Mapped[int] = mapped_column(ForeignKey("language.id" , ondelete="CASCADE"))
#     title: Mapped[str] = mapped_column(String(300))
#     description: Mapped[str] = mapped_column(Text)
#     release_year: Mapped[str] = mapped_column(DateTime , default=datetime.datetime.utcnow)
#     rental_duration: Mapped[str] = mapped_column(String(300))
#     rental_rate: Mapped[str] = mapped_column(String(300))
#     length: Mapped[int] = mapped_column()
#     replacement_cost: Mapped[int] = mapped_column()
#     rating: Mapped[int] = mapped_column()
#     last_update: Mapped[str] = mapped_column(DateTime , default=datetime.datetime.utcnow)
#     special_features: Mapped[str] = mapped_column(String(300))
#     fulltext: Mapped[str] = mapped_column(Text)
#     language : Mapped["Language"] = relationship(back_populates="films")
#
#     def __repr__(self):
#         return self.title

right_left_table = Table(
    "right_left_table",
    Base.metadata,
    Column("right_id" , ForeignKey("right_table.id")),
    Column("left_id" , ForeignKey("left_table.id"))
)


class Left_table(Base):
    __tablename__ = "left_table"
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column()
    right : Mapped[List["Right_table"]] = relationship(secondary=right_left_table , back_populates="left")

class Right_table(Base):
    __tablename__ = "right_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    left : Mapped[List["Left_table"]] = relationship(secondary=right_left_table , back_populates="right")



Base.metadata.create_all(engine)
# for post in session.query(Post).filter(Post.id == 2):
#     print(f"{post.title} {post.user}")

# for lang in session.query(Language).all():
#     print(lang.name)

# for film in session.query(Film).all():
#     print(film.language)



