FROM python:3.9

COPY ./app /app

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80
EXPOSE 5500

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
