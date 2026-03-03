FROM --platform=linux/amd64 python:3.11-slim
WORKDIR /app
COPY requirements.txt .
# increase pip network timeouts/retries to avoid transient ReadTimeout errors
RUN pip install --no-cache-dir -r requirements.txt --retries 10 --timeout 100
COPY main.py .
EXPOSE 8081
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]
