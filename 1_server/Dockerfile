ARG PYTHON_VERSION=3.6.8

FROM python:${PYTHON_VERSION}

WORKDIR /opt/server

COPY . .

EXPOSE 5000

RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "app.py"]
