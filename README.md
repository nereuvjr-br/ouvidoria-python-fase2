# Sistema de Ouvidoria Python

**Disciplina:** PROGRAMAR EM LINGUAGEM ESTRUTURADA  
**Atividade:** Entrega Final da Fase 2  
**Professor:** Daniel Abella

Este projeto é um sistema simples de Ouvidoria desenvolvido em Python, utilizando conexão com banco de dados MySQL. O objetivo é permitir que usuários registrem reclamações, elogios e sugestões.

## 📁 Arquivos do Projeto

O projeto é composto pelos seguintes arquivos principais:

*   **`menu.py`**: Arquivo principal que executa o sistema. Contém a interface de menu para interação com o usuário (CLI).
*   **`ouvidoria.py`**: Módulo que contém as regras de negócio e funções específicas da ouvidoria (listar, pesquisar, inserir, editar, excluir).
*   **`operacoesbd.py`**: Módulo responsável pela conexão genérica com o banco de dados e execução de comandos SQL.

## 🚀 Funcionalidades

O sistema oferece as seguintes opções:

1.  **Listar manifestações**: Exibe todas as manifestações cadastradas no banco de dados.
2.  **Adicionar nova manifestação**: Permite cadastrar uma nova ocorrência (Reclamação, Elogio ou Sugestão).
3.  **Pesquisar manifestação por código**: Busca os detalhes de uma manifestação específica pelo seu ID.
4.  **Editar manifestação**: Permite alterar os dados (nome, tipo, descrição) de uma manifestação existente.
5.  **Excluir manifestação**: Remove uma manifestação do sistema.
6.  **Exibir quantidade de manifestações**: Exibe o total de registros na ouvidoria.

## 🛠️ Como Executar

1.  Certifique-se de ter o Python e a biblioteca `mysql-connector-python` instalados.
2.  Configure os dados de conexão com o banco de dados no arquivo `menu.py`.
3.  Execute o arquivo principal:

```bash
python menu.py
```

## 📋 Requisitos para Funcionamento

*   Python 3.x
*   Servidor MySQL acessível
*   Tabela `ouvidoria` criada no banco de dados (ver script SQL em `db.sql` ou usar `criar_tabela.py` para inicialização).

---
*Projeto acadêmico.*
