from sqlalchemy import Column, Integer, String
from app.db import Base


class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    width = Column(Integer)
    height = Column(Integer)
    url = Column(String)
