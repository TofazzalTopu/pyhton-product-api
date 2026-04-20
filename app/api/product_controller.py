from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.product_service import ProductService
from app.schemas.product_dto import ProductRequestDTO, ProductResponseDTO

router = APIRouter(prefix="/products", tags=["Products"])

service = ProductService()

@router.post("", response_model=ProductResponseDTO)
def create_product(dto: ProductRequestDTO, db: Session = Depends(get_db)):
    return service.create_product(db, dto)


@router.get("", response_model=list[ProductResponseDTO])
def get_all_products(db: Session = Depends(get_db)):
    return service.get_all_products(db)


@router.get("/{product_id}", response_model=ProductResponseDTO)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return service.get_product(db, product_id)


@router.put("/{product_id}", response_model=ProductResponseDTO)
def update_product(product_id: int, dto: ProductRequestDTO, db: Session = Depends(get_db)):
    return service.update_product(db, product_id, dto)


# Exact match
@router.get("/by-name", response_model=ProductResponseDTO)
def get_product_by_name(
    name: str = Query(..., min_length=2),
    db: Session = Depends(get_db)
):
    return service.get_by_name(db, name)


# Partial search
@router.get("/search", response_model=List[ProductResponseDTO])
def search_products(
    name: str = Query(..., min_length=2),
    db: Session = Depends(get_db)
):
    return service.search_by_name(db, name)


@router.get("/search/pagination", response_model=List[ProductResponseDTO])
def search_products(
    name: str = Query(..., min_length=2, description="Search product by name"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return service.search_by_name(db, name, skip, limit)


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return service.delete_product(db, product_id)