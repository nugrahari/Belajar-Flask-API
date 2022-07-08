#!/usr/bin/env bash

bash $PWD/scripts/dev/down.sh
bash $PWD/scripts/dev/down-test.sh 
docker-compose up --build --detach api db-admin

docker-compose logs --follow --tail 99 api db
