from app.storage.blob import BlobStorage

if __name__ == '__main__':
    fake_storage = BlobStorage()
    fake_storage.create_container()
