FROM python:3

# Change shell to bash
SHELL [ "/bin/bash", "--login", "-c" ]

# Prevent __pycache__ folders (why?)
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Create a non-root user
ARG username=docker-user
ARG uid=1000
ARG gid=100
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER
RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --gid $GID \
    --home $HOME \
    $USER

RUN mkdir /code

# Install miniconda
USER $USER
ENV CONDA_DIR $HOME/miniconda3
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh

# Config miniconda path
ENV PATH=$CONDA_DIR/bin:$PATH
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile
RUN conda init bash

WORKDIR /code

# Get requirements file
COPY environment.yml /code/
USER root
RUN chown $UID:$GID /code/environment.yml

# Get dependencies
USER $USER
ENV ENV_PREFIX $PWD/env
RUN conda update conda
RUN conda create --prefix $ENV_PREFIX --file environment.yml
RUN conda activate $ENV_PREFIX

# Copy the code
USER root
COPY . /code/
RUN chown -R $UID:$GID /code/*

RUN apt-get update && apt-get install -y netcat
 
ENTRYPOINT ["/code/entrypoint.sh"]
