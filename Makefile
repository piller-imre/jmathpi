TRIAL=-5

build:
	podman build --rm -t apache$(TRIAL) .

run:
	podman run --detach \
		--name apache \
		--mount type=bind,source=webpage,target=/var/www/html \
		--publish 8000:80 \
		apache$(TRIAL)

console:
	podman run --rm -it \
		--name apache \
		--publish 8000:80 \
		apache$(TRIAL) /bin/bash

