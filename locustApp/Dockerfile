FROM python:latest
WORKDIR /app
RUN pip install locust
COPY test.py .
EXPOSE 80
CMD["locust", "-f", "locustfile.py", "--host", "https://thesimpsonsapi.com"]
