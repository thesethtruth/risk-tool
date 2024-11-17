FROM python:3.11-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy poetry files
COPY pyproject.toml poetry.lock ./

# Configure poetry to not create a virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-dev --no-interaction --no-ansi

# Copy application code
COPY . .

# Make start script executable
RUN chmod +x start.sh

# Expose the port the app runs on
EXPOSE 8000

# Use start script as entrypoint
CMD ["./start.sh"]
