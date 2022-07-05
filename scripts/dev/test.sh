#!/usr/bin/env bash

docker-compose exec \
    api \
    python -m pytest -v -s "$@"
    # --env CRON_API_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjU3MDAwOTUwLCJqdGkiOiJlZDkzN2FlOC1jMDhmLTQ4MDMtYTU4Mi1jMGNhNDQ4ZTcwYjciLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoxMCwidXNlcm5hbWUiOiJ6dWJhaXIifSwibmJmIjoxNjU3MDAwOTUwfQ.Wn3hI0AvTaFQJcWiAj8RwGV4QCsl9-juVCjV1k-a4RY \
