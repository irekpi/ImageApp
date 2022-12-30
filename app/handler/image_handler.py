from app.model.image import Image
from app.storage.blob import BlobStorage
from app.schema.image import ImageSchema
from app.repository.image_repo import ImageRepo
from dataclasses import dataclass
from fastapi import UploadFile
from PIL import Image as Img
from typing import List


@dataclass
class ImageHandler:
    repo = ImageRepo()
    storage = BlobStorage()

    def create(self, item: ImageSchema, uploaded_file: UploadFile) -> ImageSchema:
        new_img = self.resize(item.width, item.height, uploaded_file)
        self.storage.create_blob(file=new_img.tobytes(), name=uploaded_file.filename)
        return self.repo.create(item)

    def get(self, id_: int) -> Image:
        return self.repo.get(id_)

    def get_list(self) -> List[Image]:
        return self.repo.get_list()

    @staticmethod
    def resize(width, height, file) -> Img.Image:
        img_file = Img.open(file.file)
        return img_file.resize((width, height))
