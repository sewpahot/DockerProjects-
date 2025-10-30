# Stage 1: Builder stage for dependencies
FROM python:3.9-slim-bookworm as builder

# Set working directory and environment variables
WORKDIR /build
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=1 \
    VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create virtual environment and install build dependencies
RUN python -m venv $VIRTUAL_ENV && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.9-slim-bookworm as runtime

# Set working directory and environment variables
WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

# Copy only necessary files from builder
COPY --from=builder $VIRTUAL_ENV $VIRTUAL_ENV

# Create non-root user and set up directories
RUN groupadd -r mluser && useradd -r -g mluser -s /bin/false mluser && \
    mkdir -p data/raw data/processed models results && \
    chown -R mluser:mluser /app

# Copy only necessary project files
COPY --chown=mluser:mluser src src/
COPY --chown=mluser:mluser notebooks notebooks/
COPY --chown=mluser:mluser requirements.txt .

# Expose port and switch to non-root user
EXPOSE 8888
USER mluser

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=mlproject"]