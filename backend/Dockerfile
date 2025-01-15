FROM python:3.11-slim

WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy application code
COPY . .

# Configure poetry to not create a virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --without dev --no-interaction --no-ansi

# Make start script executable
RUN chmod +x start.sh

# Use start script as entrypoint
CMD ["./start.sh"]
