#!/bin/sh
set -ex
docker-compose run --rm -e TEST=True app pytest

