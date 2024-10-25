from pydantic import BaseModel, PositiveFloat, EmailStr, Field, field_validator
from enum import Enum
from datetime import datetime
from typing import Optional

class CategoriaBase(Enum):
    categoria1 = "Eletrônicos"
    categoria2 = "Eletrodomésticos"
    categoria3 = "Móveis e decoração"
    categoria4 = "Roupas"
    categoria5 = "Calçados"
    categoria6 = "Cama, Mesa e Banho"

class ProductBase(BaseModel):
   
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr
    

    @field_validator("categoria", check_fields=False)
    def check_categoria(cls, v):
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")
    
class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):

    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

    @field_validator("categoria", check_fields=False)
    def check_categoria(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoriaBase]:
            return v
        raise ValueError("Categoria inválida")