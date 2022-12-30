from app.repository.image_repo import ImageRepo
from app.model.image import Image
from app.schema.image import ImageSchema
from app.tests.fixtures.data import image_schema
from sqlalchemy.orm.session import Session
from unittest.mock import patch


def test_repo_init():
    repo = ImageRepo()
    assert issubclass(repo.model, Image)
    assert isinstance(repo.session, Session)


@patch('app.repository.image_repo.ImageRepo.add_')
@patch('app.repository.image_repo.session')
def test_create(mock_session, mock_add):
    repo = ImageRepo()
    repo.add_ = mock_add
    repo.session = mock_session
    obj = ImageSchema(**image_schema)
    repo.create(obj)
    mock_add.assert_called_once()
    mock_session.refresh.assert_called_once()


@patch('app.repository.image_repo.session')
def test_get(mock_session):
    repo = ImageRepo()
    repo.session = mock_session
    repo.get(1)
    mock_session.query.assert_called_once()


@patch('app.repository.image_repo.session')
@patch('app.repository.image_repo.paginate')
def test_get_list(mock_paginate, mock_session):
    repo = ImageRepo()
    repo.session = mock_session
    repo.get_list()
    mock_session.query.assert_called_once()
    mock_paginate.assert_called_once()
