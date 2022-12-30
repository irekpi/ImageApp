import pytest
from app.handler.image_handler import ImageHandler
from app.storage.blob import BlobStorage
from app.repository.image_repo import ImageRepo
from app.schema.image import ImageSchema
from app.tests.fixtures.data import image_schema
from fastapi import UploadFile
from unittest.mock import patch
from PIL import Image


def test_image_handler_init():
    handler = ImageHandler()
    assert isinstance(handler.storage, BlobStorage)
    assert isinstance(handler.repo, ImageRepo)


@patch('app.repository.image_repo.ImageRepo')
@patch('app.storage.blob.BlobStorage')
def test_create(mock_repo, mock_storage):
    handler = ImageHandler()
    handler.repo = mock_repo
    handler.storage = mock_storage
    obj = ImageSchema(**image_schema)
    with open('app/tests/fixtures/test.png', 'rb') as f:
        img = UploadFile(file=f, filename='test.png')
        handler.create(obj, img)
    mock_repo.create.assert_called_once()
    mock_storage.create_blob.assert_called_once()


@patch('app.repository.image_repo.ImageRepo')
def test_get(mock_repo):
    handler = ImageHandler()
    handler.repo = mock_repo
    handler.get(1)
    mock_repo.get.assert_called_once()


@patch('app.repository.image_repo.ImageRepo')
def test_get_list(mock_repo):
    handler = ImageHandler()
    handler.repo = mock_repo
    handler.get_list()
    mock_repo.get_list.assert_called_once()


def test_resize():
    handler = ImageHandler()
    with open('app/tests/fixtures/test.png', 'rb') as f:
        img = UploadFile(file=f, filename='test.png')
        resized = handler.resize(123, 123, img)
    assert resized.width == 123
    assert resized.height == 123
    assert isinstance(resized, Image.Image)
