import pytest
from app.model.image import Image
from app.tests.fixtures import data
from pydantic import ValidationError
from app.db import Base
from app.schema.image import ImageSchema


def test_fields():
    obj = Image(**data.image_schema)
    assert isinstance(obj, Base)


def test_fields_fail():
    img_dict = data.image_schema.copy()
    img_dict['id'] = 'fail'
    #  since SQL alchemy validates on 'action' like insert data is validated differently in this test
    with pytest.raises(ValidationError):
        obj = Image(**img_dict)
        ImageSchema(**obj.__dict__)
