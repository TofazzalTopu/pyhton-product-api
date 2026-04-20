from sqlalchemy.orm import Session
from app.model.product_model import Product

class ProductRepository:

    def save(self, db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def find_all(self, db: Session):
        return db.query(Product).all()

    def find_by_id(self, db: Session, product_id: int):
        return db.query(Product).filter(Product.id == product_id).first()
    
    def find_by_name(self, db: Session, name: str):
        return db.query(Product).filter(Product.name == name).first()

    def find_all_by_name(self, db: Session, name: str):
        return db.query(Product).filter(Product.name.ilike(f"%{name}%")).all()

    def search_by_name(self, db: Session, name: str, skip: int, limit: int):
        return (
            db.query(Product)
            .filter(Product.name.ilike(f"%{name}%"))  # case-insensitive search
            .offset(skip)
            .limit(limit)
            .all()
        )

    def delete(self, db: Session, product: Product):
        db.delete(product)
        db.commit()