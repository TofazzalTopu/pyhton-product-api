from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.product_repository import ProductRepository
from app.model.product_model import Product
from app.schemas.product_dto import ProductRequestDTO

class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    def create_product(self, db: Session, dto: ProductRequestDTO):
        product = Product(name=dto.name, price=dto.price)
        return self.repository.save(db, product)

    def get_all_products(self, db: Session):
        return self.repository.find_all(db)

    def get_product(self, db: Session, product_id: int):
        product = self.repository.find_by_id(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    
    def get_by_name(self, db: Session, name: str):
        product = self.repository.find_by_name(db, name)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

    def search_by_name(self, db: Session, name: str):
        products = self.repository.find_all_by_name(db, name)
        if not products:
            raise HTTPException(status_code=404, detail="No products found")
        return products

    def search_by_name(self, db: Session, name: str, skip: int, limit: int):
        products = self.repository.search_by_name(db, name, skip, limit)

        if not products:
            raise HTTPException(status_code=404, detail="No products found")

        return products

    def update_product(self, db: Session, product_id: int, dto: ProductRequestDTO):
        product = self.repository.find_by_id(db, product_id)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        product.name = dto.name
        product.price = dto.price

        return self.repository.save(db, product)

    def delete_product(self, db: Session, product_id: int):
        product = self.repository.find_by_id(db, product_id)

        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        self.repository.delete(db, product)
        return {"message": "Deleted successfully"}