FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
