#!/bin/bash

set -e

echo "Iniciando infraestrutura com Docker Compose..."
docker-compose up -d

sleep 10

echo "Criação da tabela de usuários (se necessário)..."
docker exec -i embrapa_db psql -U postgres -d postgres <<-EOSQL
  CREATE EXTENSION IF NOT EXISTS pgcrypto;
  CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(200) UNIQUE,
    hashed_password VARCHAR(255) NOT NULL,
    created_at VARCHAR NOT NULL
  );
EOSQL

echo "Aplicação disponível em http://localhost:8000"