from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    making_time = Column(String(100), nullable=False)
    serves = Column(String(100), nullable=False)
    ingredients = Column(String(300), nullable=False)
    cost = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
