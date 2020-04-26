FROM python:3-alpine

RUN mkdir -p /usr/src/app /usr/src/swagger-ui
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY ../swagger-ui /usr/src/swagger-ui

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
