FROM python:3.10-alpine

RUN pip install fastapi uvicorn pymongo pydantic



WORKDIR /app


COPY /app/ . 

EXPOSE 4850

CMD sh -c 'python3 seeder.py && uvicorn api:app --host 0.0.0.0 --port 4850'
