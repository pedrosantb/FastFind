FROM python:3.12.2-bookworm

RUN mkdir engine/

WORKDIR /engine

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "app:app"]