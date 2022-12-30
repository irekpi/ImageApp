from fastapi import APIRouter
from app.router.router import BaseRouter
from app.model.image import Image
from app.schema.image import ImageSchema
from app.handler.image_handler import ImageHandler
from typing import Type, List
from fastapi import UploadFile, File, HTTPException, Depends
from fastapi_pagination import Page


class ImageRouter(BaseRouter):
    def __init__(self, model: Type[ImageSchema], handler: ImageHandler):
        super().__init__(model, handler)

    def create_endpoints(self) -> APIRouter:
        router = self.set_router()

        def create(item: ImageSchema = Depends(), file: UploadFile = File(media_type='image/jpeg')) -> Image:
            if not self.validate_type(file.content_type):
                raise HTTPException(status_code=422, detail='Media type error')
            return self.handler.create(item, file)

        def get(id_: int) -> Image:
            return self.handler.get(id_)

        def get_list() -> List[Image]:
            return self.handler.get_list()

        router.add_api_route(methods=['POST'], path='/', endpoint=create)
        router.add_api_route(methods=['GET'], path='/list', endpoint=get_list, response_model=Page[ImageSchema])
        router.add_api_route(methods=['GET'], path='/{id}', endpoint=get)
        return router

    def validate_type(self, type: str) -> bool:
        img_ext = ['image/jpeg', 'image/png', 'image/jpg']
        return True if type in img_ext else False


image_router = ImageRouter(Image, ImageHandler())
