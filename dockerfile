FROM python:3.10-alpine

RUN pip install fastapi uvicorn pymongo pydantic

COPY app /

WORKDIR /app

EXPOSE 4850

CMD ["python3", "seeder.py"]

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "4850"]