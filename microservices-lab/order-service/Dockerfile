FROM --platform=linux/amd64 python:3.11-slim
WORKDIR /app
COPY requirements.txt .
# increase pip network retry and timeout to handle transient connectivity
RUN pip install --no-cache-dir -r requirements.txt --retries 10 --timeout 100
COPY . .
EXPOSE 8082
CMD ["gunicorn", "--bind", "0.0.0.0:8082", "wsgi:application"]
