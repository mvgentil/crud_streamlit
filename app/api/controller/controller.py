from sqlalchemy.orm import Session
from schemas.schemas import ProductUpdate, ProductCreate
from models.product import ProductModel


def get_product(db: Session, product_id: int):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def get_products(db: Session):
    return db.query(ProductModel).all()

def create_product(db: Session, product: ProductCreate):
    db_product = ProductCreate(**product.model_dump)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    return None

def update_product():
    return None


    