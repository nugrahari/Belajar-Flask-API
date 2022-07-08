# Sistem Rumah Sakit Delman v1

- [SRS Delman v1](#sistem-rumah-sakit-delman-v1)
  - [Prerequisite](#prerequisite)
    - [Docker](#docker)
  - [How to develop](#how-to-develop)
    - [Run services](#run-services)
    - [Run cron](#run-cron)
    - [Run pytest](#run-pytest)
    - [Reset database](#reset-database)
  - [Services](#services)

## Prerequisite

### Docker

install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)
clone [github](https://github.com/nugrahari/Belajar-Flask-API.git)

## How to develop

### Run services

> [Install docker & docker-compose](#docker) first

```sh
$ cd /path/to/project/root/dir
$ cp example.env .env
$ ./scripts/dev/up.sh
```

### Run cron

> [Install docker & docker-compose](#docker) first
> set waiting time for cron in .env file by seconds

```sh
$ cd /path/to/project/root/dir
$ ./scripts/dev/cron.sh
```

### Run pytest

> [Install docker & docker-compose](#docker) first

1. run service for testing :
```sh
$ cd /path/to/project/root/dir
$ ./scripts/dev/up-test.sh
```
2. create user, password and database for testing
```sql
CREATE USER srs_test WITH PASSWORD 'srs_test';
CREATE DATABASE srs_test;
GRANT ALL PRIVILEGES ON DATABASE srs_test TO srs_test;
```
3. run pytest

```sh
$ cd /path/to/project/root/dir
$ ./scripts/dev/test.sh
```

### Reset database

> [Install docker & docker-compose](#docker) first

```sh
$ cd /path/to/project/root/dir
$ ./scripts/dev/reset-db.sh
```

## Services

- [api](http://localhost:28088)
- [db admin](http://localhost:8081)
