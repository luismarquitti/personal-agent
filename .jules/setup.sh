#!/bin/bash
# .jules/setup.sh - Script de configuração para o ambiente Google Jules (Ubuntu)

echo "==> Iniciando configuração do ambiente Jules..."

# 1. Configuração do Node.js (Root)
echo "==> Instalando dependências do Node.js (Root)..."
npm install

# 2. Configuração do Frontend (Web)
echo "==> Instalando dependências do Frontend (Web)..."
cd web && npm install && cd ..

# 3. Configuração do Python (Backend)
echo "==> Criando ambiente virtual Python..."
python3 -m venv .venv
source .venv/bin/activate
echo "==> Instalando dependências do Python..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Configuração de Variáveis de Ambiente
if [ ! -f .env ]; then
    echo "==> Criando arquivo .env a partir do .env.example..."
    if [ -f .env.example ]; then
        cp .env.example .env
    else
        echo "DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/personal_ai_core" > .env
        echo "DB_HOST=localhost" >> .env
        echo "DB_PORT=5432" >> .env
        echo "DB_NAME=personal_ai_core" >> .env
        echo "DB_USER=postgres" >> .env
        echo "DB_PASSWORD=yourpassword" >> .env
    fi
fi

# 5. Inicialização de Serviços (Opcional, se o Jules permitir Docker background)
echo "==> Tentando subir o banco de dados via Docker Compose..."
docker compose up -d

# 6. Diagnóstico Final
echo "==> Executando script de diagnóstico (doctor.py)..."
python3 scripts/doctor.py

echo "==> Setup concluído com sucesso!"
