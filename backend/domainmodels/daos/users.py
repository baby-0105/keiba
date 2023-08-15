from sqlalchemy import Column, Integer, String

from database import Base


class UsersModel(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
    )
    name = Column(String(40))
