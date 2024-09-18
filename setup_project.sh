#!/bin/bash
# Buildando o sintetizado
docker build -t sintetizador_rust .
docker run \
    -v ./sintetizador:/home/sintetizador \
    sintetizador_rust

cp ./sintetizador/target/release/main compilador/sintetizador
mkdir -p wav

# Instalando as dependências
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt