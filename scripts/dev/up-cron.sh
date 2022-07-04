#!/usr/bin/env bash


docker-compose -f docker-compose-cron.yaml up --build --detach 

docker-compose -f docker-compose-cron.yaml logs --follow --tail 99 
