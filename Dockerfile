FROM python:3.11-slim
WORKDIR /app
COPY cipher.py .
ENTRYPOINT ["python", "cipher.py"]