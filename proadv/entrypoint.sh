#!/bin/bash

# Wait for database initialization
echo "Waiting for database..."

while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
    sleep 0.1
done

echo "PostgreSQL detected"
echo ""

exec "$@"
