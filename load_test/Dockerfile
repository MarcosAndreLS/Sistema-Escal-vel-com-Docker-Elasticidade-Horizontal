FROM python:3.10-slim

WORKDIR /load_test
COPY app/requirements.txt /load_test/
RUN pip install -r requirements.txt

COPY load_test/locustfile.py .

CMD ["locust", "-f", "locustfile.py", "--host", "http://flask1:5000"]
