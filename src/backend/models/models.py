from sqlalchemy import Column, String, Float, DateTime, Integer
from sqlalchemy import func
from db.database import Base
import uuid

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    categoria = Column(String, index=True)
    email_fornecedor = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), default=func.now(), index=True)
