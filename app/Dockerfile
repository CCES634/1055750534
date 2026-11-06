FROM python:latest
WORKDIR /app
COPY requeriments.txt .
RUN pip install --no-cache-dir -r requeriments.txt
COPY app.py .
CMD ["python", "app.py"]
