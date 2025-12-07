from operacoesbd import *

# Função para listar todas as manifestações cadastradas na ouvidoria
def listarManifestacoes(conexao):
    # Cria a consulta SQL para selecionar todos os registros da tabela ouvidoria
    consulta = "select * from ouvidoria"
    # Chama a função genérica de listar do arquivo operacoesbd
    resultado = listarBancoDados(conexao, consulta)
    return resultado

# Função para pesquisar uma manifestação específica pelo seu código
def pesquisarManifestacaoPorCodigo(conexao, codigo):
    # Cria a consulta SQL com um filtro pelo código (usando %s para evitar SQL Injection)
    consulta = "select * from ouvidoria where codigo = %s"
    # Define os parâmetros para a consulta
    dados = [codigo]
    # Chama a função de listar passando os parâmetros
    resultados = listarBancoDados(conexao, consulta, dados)
    
    # Verifica se encontrou algum resultado
    if len(resultados) > 0:
        # Retorna o primeiro (e único) resultado encontrado
        return resultados[0]
    else:
        # Retorna None caso não encontre
        return None

# Função para inserir uma nova manifestação na ouvidoria
def inserirManifestacao(conexao, nome, tipo, descricao):
    # Cria a consulta SQL de inserção
    consulta = "insert into ouvidoria (nome, tipo, descricao) values (%s, %s, %s)"
    # Prepara a lista de dados a serem inseridos
    dados = [nome, tipo, descricao]
    # Chama a função de inserção e retorna o ID do novo registro
    id_novo = insertNoBancoDados(conexao, consulta, dados)
    return id_novo

# Função para excluir uma manifestação do banco de dados pelo código
def excluirManifestacao(conexao, codigo):
    # Cria a consulta SQL de exclusão
    consulta = "delete from ouvidoria where codigo = %s"
    # Define o parâmetro do código a ser excluído
    dados = [codigo]
    # Chama a função de exclusão e retorna a quantidade de linhas afetadas
    linhas_afetadas = excluirBancoDados(conexao, consulta, dados)
    return linhas_afetadas

# Função para atualizar os dados de uma manifestação existente
def atualizarManifestacao(conexao, codigo, nome, tipo, descricao):
    # Cria a consulta SQL de atualização
    consulta = "update ouvidoria set nome = %s, tipo = %s, descricao = %s where codigo = %s"
    # Prepara os dados, lembrando que o código vai por último devido à ordem no SQL
    dados = [nome, tipo, descricao, codigo]
    # Chama a função de atualização e retorna a quantidade de linhas afetadas
    linhas_afetadas = atualizarBancoDados(conexao, consulta, dados)
    return linhas_afetadas

# Função para contar a quantidade de manifestações cadastradas
def contarManifestacoes(conexao):
    # Cria a consulta SQL para contar os registros
    consulta = "select count(*) from ouvidoria"
    # Chama a função de listar que retorna uma lista de tuplas
    resultado = listarBancoDados(conexao, consulta)
    
    if len(resultado) > 0:
        # Retorna o primeiro elemento da primeira tupla (o count)
        return resultado[0][0]
    else:
        return 0
