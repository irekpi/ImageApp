from pydantic import BaseModel, root_validator
from typing import Optional


class ImageSchema(BaseModel):
    id: int
    title: str
    width: int
    height: int
    url: Optional[str]

    class Config:
        orm_mode = True
