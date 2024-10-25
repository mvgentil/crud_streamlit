from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal, get_db
from schemas.schemas import ProductCreate, ProductResponse, ProductUpdate
from typing import List
from controller.controller import (
    create_product,
    get_product,
    get_products,
    delete_product,
    update_product
)

router = APIRouter()

@router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product=product)