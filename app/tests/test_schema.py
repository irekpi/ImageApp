import pytest
from app.schema.image import ImageSchema
from app.tests.fixtures import data
from pydantic import BaseModel, ValidationError


def test_fields():
    obj = ImageSchema(**data.image_schema)
    assert isinstance(obj, BaseModel)


def test_fields_fail():
    img_dict = data.image_schema.copy()
    img_dict['id'] = 'fail'
    with pytest.raises(ValidationError):
        obj = ImageSchema(**img_dict)
