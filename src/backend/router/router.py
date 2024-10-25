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

@router.get("/products/", response_model=List[ProductResponse])
def get_products_route(db: Session = Depends(get_db)):
    return get_products(db=db)

@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product_by_id_route(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return db_product

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return db_product

@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    db_product = delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product Not Found")
    return db_product