#!/bin/sh

echo "Waiting for PostgreSQL..."

until python -c "
import socket
s = socket.socket()
s.connect(('postgres',5432))
print('Database Ready')
"
do
    sleep 2
done

echo "Running Database Migration..."

alembic upgrade head

echo "Starting FastAPI..."

exec gunicorn app.main:app \
    -k uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --workers 4