#!/bin/sh
#
#if [ "$DATABASE" = "redis" ]
#then
#    echo "Waiting for Redis..."
#
#    while ! nc -z $REDIS_HOST $REDIS_PORT; do
#      sleep 0.1
#    done
#
#    echo "Redis started"
#fi
#
#exec "$@"