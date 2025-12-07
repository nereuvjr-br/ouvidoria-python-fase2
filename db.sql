-- Script de Criação do Banco de Dados e Tabela

-- Criação do Banco de Dados
CREATE SCHEMA `ouvidoria` ;

-- Seleção do Banco de Dados
USE ouvidoria;

-- Criação da Tabela ouvidoria
CREATE TABLE IF NOT EXISTS ouvidoria (
    codigo INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descricao TEXT NOT NULL
);
