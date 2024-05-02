from resources import db

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String,TIMESTAMP


class BookModel(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    name:Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    author:Mapped[str] = mapped_column(String(255), nullable=False) 
    public_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False) 

    
