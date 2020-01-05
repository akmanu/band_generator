# an argument for the python version
# by default this is for version 3.6.8, but it can be modified
ARG PYTHON_VERSION=3.6.8

# the base image to build from with python version passed through
FROM python:${PYTHON_VERSION}

# set the working directory
WORKDIR /opt/server

# copy files from context to working directory
# .dockerignore is used to ignore any files you don't want to copy over
COPY . .

# app will run on port 5001
EXPOSE 5001

# install dependencies
RUN pip install -r requirements.txt

# run traditionally
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
