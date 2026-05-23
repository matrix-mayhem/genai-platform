# -------- Stage 1: Builder --------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv

# Activate venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# -------- Stage 2: Runtime --------
FROM python:3.11-slim

WORKDIR /app

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv

# Activate venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]