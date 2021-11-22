FROM python:3.8-alpine
COPY . .
RUN apk add --no-cache postgresql-libs
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev 
RUN pip install -r requirements.txt
CMD uvicorn main:app --host 0.0.0.0