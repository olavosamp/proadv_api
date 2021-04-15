FROM python:3

# Prevent __pycache__ folders (why?)
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Make a new directory to put our code in.
WORKDIR /code/

# Install system dependencies
RUN apt-get update && apt-get install -y netcat gettext

# Install code dependencies
COPY ./requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy data
RUN mkdir /data/
COPY ./data/ /data/

# Copy the code
COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]
