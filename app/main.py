from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.product_controller import router as product_router
from app.api.item_controller import itemRouter as item_router
from fastapi.middleware.cors import CORSMiddleware

#  Create app ONLY ONCE
app = FastAPI(title="Product API")

# CORS config
origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB init
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(product_router)
app.include_router(item_router)