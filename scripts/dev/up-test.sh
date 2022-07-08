#!/usr/bin/env bash

bash $PWD/scripts/dev/down.sh 
bash $PWD/scripts/dev/down-test.sh 
docker-compose -f docker-compose-test.yaml up --build --detach 
docker-compose -f docker-compose-test.yaml logs --follow --tail 99 api_test 