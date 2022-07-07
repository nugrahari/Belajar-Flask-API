#!/usr/bin/env bash

docker-compose -f docker-compose-test.yaml exec \
    api_test \
    python -m pytest -v -s "$@"
    # --env TEST='true' \
