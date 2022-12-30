# Simple Image App

### Base
    
    Simple backend application for managing images.
    
    Project URLS are base on FASTAPI docs:
        - Base urls can be found in: http://0.0.0.0:8000/docs

    Project:
        - is based on Docker, docker-compose
        - uses Makefile
        - uses Fake Azure Blob Storage - Azurite (which needs to be initiated with Makefile script)
        - uses SQLite
        - uses Poetry as packages manager
        
    Poetry includes:
        - python = "^3.10"
        - fastapi = "^0.88.0"
        - uvicorn = "^0.20.0"
        - pydantic = "^1.10.2"
        - sqlalchemy = "^1.4.45"
        - databases = {extras = ["sqlite"], version = "^0.7.0"}
        - python-multipart = "^0.0.5"
        - fastapi-pagination = "^0.11.1"
        - azure-storage-blob = "^12.14.1"
        - pillow = "^9.3.0"
        - pytest = "^7.2.0"


### Building

Project is operated via Makefile. Base commands are presented below:

Docker

    $ make up          # Create and start container
    $ make console     # Opens main app container
    $ make build       # Build or rebuild services (force-recreate, no-cache and others omitted)
Fake Blob Container creation:

    $ make create_blob  # Django Migrations

Tests
    
    $ make test        # Run unittests 

