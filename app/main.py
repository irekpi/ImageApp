from fastapi import FastAPI
from app.db import engine
from app.model import image
from app.router.image_router import image_router
from fastapi_pagination import add_pagination

image.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(image_router.create_endpoints())

add_pagination(app)
