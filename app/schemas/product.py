# app/schemas/product.py

from decimal import Decimal
from datetime import datetime

from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=150,
        description="Product name"
    )

    description: str | None = Field(
        default=None,
        max_length=500,
        description="Product description"
    )

    price: Decimal = Field(
        ...,
        gt=0,
        decimal_places=2,
        description="Product price"
    )

    stock: int = Field(
        default=0,
        ge=0,
        description="Available stock"
    )

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=150
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )

    price: Decimal | None = Field(
        default=None,
        gt=0,
        decimal_places=2
    )

    stock: int | None = Field(
        default=None,
        ge=0
    )

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }