#!/bin/bash

docker run \
    -e POSTGRES_USER=infoboardv2-admin \
    -e POSTGRES_PASSWORD=changeme \
    -e POSTGRES_DB=infoboardv2\
    -e POSTGRES_SCHEMA=infoboardv2 \
    -p 5432:5432 \
    -v ~/docker_volumes/postgres-data/izy-infoboardv2:/var/lib/postgresql/data \
    -d -t -i --name izy-infoboardv2-postgres izy-infoboardv2-postgres
