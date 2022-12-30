# Use in order to access different app features
# Opens main app container
console:
	sudo docker exec -it app /bin/bash
# Create and start container
up:
	sudo docker-compose up
# Build or rebuild services (force-recreate, no-cache and others omitted)
build:
	sudo docker-compose up --build
# Creates fake Azure BlobStorage for tests
create_blob:
	sudo docker exec -it app python -m app.storage.create_fake_blob

# Run unittests
test:
	docker exec -it app poetry run pytest app/tests/ --capture=no