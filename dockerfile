FROM ubuntu:22.04

# Setting up rust environment
WORKDIR /bin/rust
RUN apt update && apt install curl build-essential -y
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs >> instalation_script
RUN chmod +x instalation_script
RUN ./instalation_script -y
ENV PATH="/bin/rust/bin:$PATH"

# Setting up python environment
RUN apt update && apt install python3 python3-pip python3-venv -y
RUN python3 -m venv /opt/antlr/antlr-venv
ENV PATH="/opt/antlr/antlr-venv/bin:$PATH"
COPY requirements.txt .
RUN /opt/antlr/antlr-venv/bin/python -m pip install -r requirements.txt

WORKDIR /home
COPY ./sintetizador .
COPY ./run .