from pydantic import BaseModel, Field, field_validator
from typing import Annotated


class ProductRequestDTO(BaseModel):
    name: Annotated[
        str,
        Field(
            ...,
            min_length=2,
            max_length=100,
            description="Product name (2–100 chars)"
        )
    ]

    price: Annotated[
        float,
        Field(
            ...,
            gt=0,
            le=100000,
            description="Product price (>0 and <=100000)"
        )
    ]

    # Custom validation (business rule)
    @field_validator("name")
    @classmethod
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError("Name cannot be empty or whitespace")
        return v


class ProductResponseDTO(BaseModel):
    id: int
    name: Annotated[
        str,
        Field(min_length=2, max_length=100)
    ]

    price: Annotated[
        float,
        Field(gt=0)
    ]

    class Config:
        from_attributes = True