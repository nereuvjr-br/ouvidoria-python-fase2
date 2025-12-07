from operacoesbd import *
from ouvidoria import *

# Inicializa a opção com um valor diferente de saída
opcao = -1
# Cria a conexão com o banco de dados 'ouvidoria'
# Caso o nome do banco seja diferente, altere o último parâmetro
conexao = criarConexao('143.110.133.149', 'root', 'aslkjhdlru', 'ouvidoria')

# Loop principal do menu
while opcao != 7:
    print("\n--- Sistema de Ouvidoria ---")
    print("1) Listar manifestações")
    print("2) Adicionar nova manifestação")
    print("3) Pesquisar manifestação por código")
    print("4) Editar manifestação")
    print("5) Excluir manifestação")
    print("6) Exibir quantidade de manifestações")
    print("7) Sair")
    
    try:
        opcao = int(input("Digite a sua opção: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    # Opção 1: Listar
    if opcao == 1:
        lista = listarManifestacoes(conexao)
        
        if len(lista) == 0:
            print("\nNenhuma manifestação encontrada.")
        else:
            print("\n--- Lista de Manifestações ---")
            for item in lista:
                # O item é uma tupla, ex: (codigo, nome, tipo, descricao)
                # Ajuste os índices conforme a ordem das colunas no seu banco
                print(f"Código: {item[0]} | Nome: {item[1]} | Tipo: {item[2]}")
                print(f"Descrição: {item[3]}")
                print("-" * 30)

    # Opção 2: Adicionar
    elif opcao == 2:
        print("\n--- Nova Manifestação ---")
        nome = input("Digite o nome do requerente: ")
        print("\nSelecione o tipo da manifestação:")
        print("1) Reclamação")
        print("2) Elogio")
        print("3) Sugestão")
        opcao_tipo = input("Digite o número da opção do tipo: ")

        if opcao_tipo == '1':
            tipo = 'Reclamação'
        elif opcao_tipo == '2':
            tipo = 'Elogio'
        elif opcao_tipo == '3':
            tipo = 'Sugestão'
        else:
            tipo = 'Outros'
            print("Opção inválida. Definido como 'Outros'.")
        descricao = input("Digite a descrição da manifestação: ")
        
        novo_id = inserirManifestacao(conexao, nome, tipo, descricao)
        
        if novo_id:
            print(f"Manifestação inserida com sucesso! Código gerado: {novo_id}")

    # Opção 3: Pesquisar
    elif opcao == 3:
        try:
            codigo = int(input("Digite o código da manifestação: "))
            item = pesquisarManifestacaoPorCodigo(conexao, codigo)
            
            if item:
                print("\n--- Detalhes da Manifestação ---")
                print(f"Código: {item[0]}")
                print(f"Nome: {item[1]}")
                print(f"Tipo: {item[2]}")
                print(f"Descrição: {item[3]}")
            else:
                print("Manifestação não encontrada para o código informado.")
        except ValueError:
            print("O código deve ser um número inteiro.")

    # Opção 4: Editar
    elif opcao == 4:
        try:
            codigo = int(input("Digite o código da manifestação que deseja editar: "))
            # Primeiro verificamos se existe
            item = pesquisarManifestacaoPorCodigo(conexao, codigo)
            
            if item:
                print(f"Editando manifestação de: {item[1]}")
                novo_nome = input("Digite o novo nome: ")
                print("\nSelecione o novo tipo da manifestação:")
                print("1) Reclamação")
                print("2) Elogio")
                print("3) Sugestão")
                opcao_tipo = input("Digite o número da opção do novo tipo: ")

                if opcao_tipo == '1':
                    novo_tipo = 'Reclamação'
                elif opcao_tipo == '2':
                    novo_tipo = 'Elogio'
                elif opcao_tipo == '3':
                    novo_tipo = 'Sugestão'
                else:
                    novo_tipo = 'Outros'
                    print("Opção inválida. Definido como 'Outros'.")

                nova_descricao = input("Digite a nova descrição: ")
                
                linhas = atualizarManifestacao(conexao, codigo, novo_nome, novo_tipo, nova_descricao)
                
                if linhas > 0:
                    print("Manifestação atualizada com sucesso!")
                else:
                    print("Erro ao atualizar a manifestação.")
            else:
                print("Manifestação não encontrada.")
        except ValueError:
            print("O código deve ser um número inteiro.")

    # Opção 5: Excluir
    elif opcao == 5:
        try:
            codigo = int(input("Digite o código da manifestação que deseja excluir: "))
            # Podemos verificar se existe antes ou tentar excluir direto
            linhas = excluirManifestacao(conexao, codigo)
            
            if linhas > 0:
                print("Manifestação excluída com sucesso!")
            else:
                print("Nenhuma manifestação foi excluída (verifique o código).")
        except ValueError:
            print("O código deve ser um número inteiro.")

    # Opção 6: Contar Quantidade
    elif opcao == 6:
        quantidade = contarManifestacoes(conexao)
        print(f"\nQuantidade total de manifestações: {quantidade}")

    # Opção 7: Sair
    elif opcao == 7:
        print("Saindo do sistema...")
    
    else:
        print("Opção inválida! Tente novamente.")

# Encerra a conexão ao final
encerrarConexao(conexao)
print("Programa finalizado.")
