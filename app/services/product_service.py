from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

def create_product(db: Session, data: ProductCreate):
    existing_product = (
        db.query(Product)
        .filter(Product.name == data.name)
        .first()
    )

    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product already exists"
        )

    product = Product(
        name=data.name,
        description=data.description,
        price=data.price,
        stock=data.stock
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

def get_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )

    return product

def update_product(
    db: Session,
    product_id: int,
    data: ProductUpdate
):
    product = get_product_by_id(db, product_id)

    if data.name is not None:
        existing_product = (
            db.query(Product)
            .filter(
                Product.name == data.name,
                Product.id != product_id
            )
            .first()
        )

        if existing_product:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A product with this name already exists"
            )

        product.name = data.name                # type: ignore

    if data.description is not None:
        product.description = data.description  # type: ignore

    if data.price is not None:
        product.price = data.price              # type: ignore

    if data.stock is not None:
        product.stock = data.stock              # type: ignore

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int):
    product = get_product_by_id(db, product_id)

    db.delete(product)
    db.commit()

    return {
        "message": "Product deleted successfully"
    }