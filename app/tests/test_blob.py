from unittest.mock import patch
from app.storage.blob import BlobStorage


@patch('app.storage.blob.ContainerClient')
def test_create_blob(mock_client):
    storage = BlobStorage()
    with open('app/tests/fixtures/data.py', 'r') as f:
        storage.create_blob(f, 'test', container_name='test1')
    mock_client.from_connection_string.assert_called_once()


@patch('app.storage.blob.BlobServiceClient')
def test_create_container(mock_client):
    storage = BlobStorage()
    storage.create_container('test')
    mock_client.from_connection_string.assert_called_once()
