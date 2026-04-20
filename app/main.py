from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.product_controller import router as product_router
from app.api.item_controller import itemRouter as item_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product API")

app.include_router(product_router)
app.include_router(item_router)