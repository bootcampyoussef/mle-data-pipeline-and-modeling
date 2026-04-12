FROM python:3.11.13-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt

COPY data_ingestion.py .

ENTRYPOINT ["python", "data_ingestion.py"]
