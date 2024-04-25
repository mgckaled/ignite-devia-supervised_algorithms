FROM python:3.11.3

WORKDIR /code/apps/m12

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./apps/m12 /code/apps/m12/

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port" "80" ]