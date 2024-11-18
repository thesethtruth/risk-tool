#!/bin/bash

# Function to test if MySQL is ready
wait_for_mysql() {
    echo "Waiting for MySQL to be ready..."
    while ! poetry run python -c "
import pymysql
try:
    pymysql.connect(
        host='db',
        user='user',
        password='password',
        database='risk_tool'
    ).close()
    print('MySQL is ready')
    exit(0)
except Exception as e:
    exit(1)
"
    do
        echo "MySQL is unavailable - sleeping"
        sleep 1
    done
}

# Wait for MySQL
wait_for_mysql

# Run migrations
echo "Running database migrations..."
poetry run alembic upgrade head

# Start the application
echo "Starting FastAPI application..."
poetry run uvicorn app:app --host 0.0.0.0 --port 5000
