FROM python:3

# Change shell to bash
SHELL [ "/bin/bash", "--login", "-c" ]

# Prevent __pycache__ folders (why?)
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install miniconda
ENV CONDA_DIR $HOME/miniconda3
RUN wget -q https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh

# Config miniconda path
ENV PATH=$CONDA_DIR/bin:$PATH
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile
RUN conda init bash

# Create project folder
RUN mkdir /code
WORKDIR /code

# Get requirements file
COPY environment.yml /code/

# Get dependencies
ENV ENV_PREFIX $PWD/env
RUN conda update conda
RUN conda env create --prefix $ENV_PREFIX --file environment.yml
RUN conda activate $ENV_PREFIX

RUN apt-get update && apt-get install -y netcat

# Copy the code
COPY . /code/

ENTRYPOINT ["/code/entrypoint.sh"]
