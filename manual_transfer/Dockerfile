FROM python:3.9-slim

WORKDIR /manual_transfer

COPY app/requirements.txt /manual_transfer/
RUN pip install -r requirements.txt

COPY manual_transfer/manual_router.py .

CMD ["python", "manual_router.py"]
