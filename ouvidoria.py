from operacoesbd import *

# --- Métodos de Banco de Dados ---

# Função responsável por listar todas as manifestações existentes no banco de dados
# Retorna uma lista de tuplas com os dados recuperados
def listarManifestacoes(conexao):
    consulta = "select * from ouvidoria"
    # Chama a função genérica que executa o SELECT sem parâmetros
    resultado = listarBancoDados(conexao, consulta)
    return resultado

# Função responsável por buscar uma única manifestação pelo seu código (ID)
# Retorna a tupla com os dados da manifestação ou None se não encontrar
def pesquisarManifestacaoPorCodigo(conexao, codigo):
    consulta = "select * from ouvidoria where codigo = %s"
    dados = [codigo]
    # Chama a função genérica passando o código como parâmetro para a consulta
    resultados = listarBancoDados(conexao, consulta, dados)
    
    # Se a lista de resultados não estiver vazia, retorna o primeiro item
    if len(resultados) > 0:
        return resultados[0]
    else:
        return None

# Função responsável por inserir uma nova manifestação no banco de dados
# Recebe os dados (nome, tipo, descricao) e retorna o ID do novo registro
def inserirManifestacao(conexao, nome, tipo, descricao):
    consulta = "insert into ouvidoria (nome, tipo, descricao) values (%s, %s, %s)"
    dados = [nome, tipo, descricao]
    # Chama a função genérica de insert que executa o INSERT e retorna o lastrowid
    id_novo = insertNoBancoDados(conexao, consulta, dados)
    return id_novo

# Função responsável por excluir uma manifestação do banco de dados
# Recebe o código e retorna a quantidade de linhas afetadas (1 se sucesso, 0 se falha)
def excluirManifestacao(conexao, codigo):
    consulta = "delete from ouvidoria where codigo = %s"
    dados = [codigo]
    # Chama a função genérica de exclusão
    linhas_afetadas = excluirBancoDados(conexao, consulta, dados)
    return linhas_afetadas

# Função responsável por atualizar os dados de uma manifestação existente
# Recebe o código e os novos dados, retornando a quantidade de linhas afetadas
def atualizarManifestacao(conexao, codigo, nome, tipo, descricao):
    consulta = "update ouvidoria set nome = %s, tipo = %s, descricao = %s where codigo = %s"
    dados = [nome, tipo, descricao, codigo] # O código é o último parâmetro na query
    # Chama a função genérica de atualização
    linhas_afetadas = atualizarBancoDados(conexao, consulta, dados)
    return linhas_afetadas

# Função responsável por contar quantas manifestações existem cadastradas
# Retorna um número inteiro com o total
def contarManifestacoes(conexao):
    consulta = "select count(*) from ouvidoria"
    resultado = listarBancoDados(conexao, consulta)
    
    # O resultado vem como uma lista de tuplas, ex: [(5,)]
    if len(resultado) > 0:
        return resultado[0][0] # Pega o primeiro elemento da primeira tupla
    else:
        return 0

# --- Métodos Auxiliares de Interface (IO) ---

# Função auxiliar para ler e validar o tipo de manifestação escolhido pelo usuário
# Exibe um menu, lê a entrada e retorna a string correspondente ('Reclamação', etc.)
def lerTipoManifestacao(mensagem="Selecione o tipo da manifestação:"):
    print("\n" + mensagem)
    print("1) Reclamação")
    print("2) Elogio")
    print("3) Sugestão")
    opcao = input("Digite o número da opção: ")

    if opcao == '1':
        return 'Reclamação'
    elif opcao == '2':
        return 'Elogio'
    elif opcao == '3':
        return 'Sugestão'
    else:
        print("Opção inválida. Definido como 'Outros'.")
        return 'Outros'

# Função auxiliar para exibir os dados de uma manifestação de forma formatada
# Recebe uma tupla 'item' vinda do banco de dados (codigo, nome, tipo, descricao)
def exibirManifestacao(item):
    print(f"Código: {item[0]} | Nome: {item[1]} | Tipo: {item[2]}")
    print(f"Descrição: {item[3]}")
    print("------------------------------")
