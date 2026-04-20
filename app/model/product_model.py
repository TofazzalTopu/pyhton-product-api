from numbers import Number
from sqlalchemy import CheckConstraint, Column, Integer, Numeric, String
from app.core.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

    __table_args__ = (
        CheckConstraint("length(name) >= 2", name="check_name_min_length"),
        CheckConstraint("price > 0", name="check_price_positive"),
    )