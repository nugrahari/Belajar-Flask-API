#!/usr/bin/env bash


docker-compose -f docker-compose-test.yaml down "$@"
docker-compose -f docker-compose-test.yaml up --build --detach 
docker-compose -f docker-compose-test.yaml logs --follow --tail 99 api_test 