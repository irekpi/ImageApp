from app.db import SessionLocal
from app.db import session
from app.model.image import Image
from app.schema.image import ImageSchema
from typing import List
from fastapi_pagination.ext.sqlalchemy import paginate


class ImageRepo:
    def __init__(self, model: Image = Image, session: SessionLocal = session):
        self.session = session
        self.model = model

    def create(self, item: ImageSchema) -> Image:
        image = Image(**item.dict())
        self.add_(image)
        self.session.refresh(image)
        return image

    def get(self, id_: int) -> Image:
        return self.session.query(Image).filter(Image.id == id_).first()

    def get_list(self) -> List[Image]:
        return paginate(self.session.query(Image).order_by(Image.title))

    def add_(self, item):
        try:
            self.session.add(item)
            self.session.commit()
        except:
            self.session.rollback()
            raise
