#!/usr/bin/env bash

# Run DB migration
flask db init
flask db migrate
flask db upgrade

# Pass execution to Main container process (set by RUN directive)
exec "$@"