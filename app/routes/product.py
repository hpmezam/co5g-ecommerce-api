from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.product import (
    ProductCreate,
    ProductResponse,
    ProductUpdate
)

from app.services.product_service import (
    create_product,
    get_products,
    get_product_by_id,
    update_product,
    delete_product
)

from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_product(db, data)

@router.get(
    "",
    response_model=list[ProductResponse]
)
def list_products(
    db: Session = Depends(get_db)
):
    return get_products(db)

@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_by_id(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_product_by_id(db, product_id)

@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return update_product(
        db,
        product_id,
        data
    )

@router.delete("/{product_id}")
def delete(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return delete_product(db, product_id)