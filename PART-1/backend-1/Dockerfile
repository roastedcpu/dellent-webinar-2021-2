FROM python:3.8-alpine
COPY . .
RUN pip install -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0