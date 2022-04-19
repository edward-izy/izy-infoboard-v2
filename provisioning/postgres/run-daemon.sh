#!/bin/bash

docker run \
    -e POSTGRES_USER=infoboard-admin \
    -e POSTGRES_PASSWORD=changeme \
    -e POSTGRES_DB=infoboard\
    -e POSTGRES_SCHEMA=infoboard \
    -p 5432:5432 \
    -v ~/docker_volumes/postgres-data/izy-infoboard:/var/lib/postgresql/data \
    -d -t -i --name izy-infoboard-postgres izy-infoboard-postgres
