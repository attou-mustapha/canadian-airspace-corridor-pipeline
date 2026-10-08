FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gdal-bin \
    libgdal-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY pyproject.toml .
RUN pip install --upgrade pip && pip install .
COPY . .

CMD ["uvicorn", "airspace_pipeline.api:app", "--host", "0.0.0.0", "--port", "8000"]
