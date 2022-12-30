from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import ContainerClient, BlobServiceClient
from app.settings import settings


class BlobStorage:
    def create_blob(self, file, name, container_name='test1'):
        container = ContainerClient.from_connection_string(settings.BLOB_CONN_STR, container_name=container_name)
        try:
            container.upload_blob(data=file, name=name)
        except ResourceExistsError:
            raise Exception('Blob already exists')

    def create_container(self, container_name='test1'):
        blob_service = BlobServiceClient.from_connection_string(settings.BLOB_CONN_STR)
        try:
            blob_service.create_container(container_name)
        except ResourceExistsError:
            raise Exception('Blob container already exists')
