FROM python:3.6.9-slim

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD ["gunicorn"  , "-w", "4", "-b", "0.0.0.0:8081",  "--access-logfile", "guni.log", "app.run:create_app()"]