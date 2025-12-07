from ouvidoria import * #Importa as funções do arquivo ouvidoria.py
from operacoesbd import *


# Inicializa a opção com um valor diferente de saída
opcao = -1
# Cria a conexão com o banco de dados
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
    
    entrada_opcao = input("Digite a sua opção: ")
    if entrada_opcao.isdigit():
        opcao = int(entrada_opcao)
    else:
        print("Por favor, digite um número válido.")
        opcao = -1

    # Opção 1: Listar
    if opcao == 1:
        lista = listarManifestacoes(conexao)
        
        if len(lista) == 0:
            print("\nNenhuma manifestação encontrada.")
        else:
            print("\n--- Lista de Manifestações ---")
            for item in lista:
                exibirManifestacao(item)

    # Opção 2: Adicionar
    elif opcao == 2:
        print("\n--- Nova Manifestação ---")
        nome = input("Digite o nome do requerente: ")
        tipo = lerTipoManifestacao("Selecione o tipo da manifestação:")
        descricao = input("Digite a descrição da manifestação: ")
        
        novo_id = inserirManifestacao(conexao, nome, tipo, descricao)
        
        if novo_id:
            print(f"Manifestação inserida com sucesso! Código gerado: {novo_id}")

    # Opção 3: Pesquisar
    elif opcao == 3:
        entrada_codigo = input("Digite o código da manifestação: ")
        if entrada_codigo.isdigit():
            codigo = int(entrada_codigo)
            item = pesquisarManifestacaoPorCodigo(conexao, codigo)
            
            if item:
                print("\n--- Detalhes da Manifestação ---")
                exibirManifestacao(item)
            else:
                print("Manifestação não encontrada para o código informado.")
        else:
            print("O código deve ser um número inteiro.")

    # Opção 4: Editar
    elif opcao == 4:
        entrada_codigo = input("Digite o código da manifestação que deseja editar: ")
        if entrada_codigo.isdigit():
            codigo = int(entrada_codigo)
            # Primeiro verificamos se existe
            item = pesquisarManifestacaoPorCodigo(conexao, codigo)
            
            if item:
                print(f"Editando manifestação de: {item[1]}")
                novo_nome = input("Digite o novo nome: ")
                novo_tipo = lerTipoManifestacao("Selecione o novo tipo da manifestação:")
                nova_descricao = input("Digite a nova descrição: ")
                
                linhas = atualizarManifestacao(conexao, codigo, novo_nome, novo_tipo, nova_descricao)
                
                if linhas > 0:
                    print("Manifestação atualizada com sucesso!")
                else:
                    print("Erro ao atualizar a manifestação.")
            else:
                print("Manifestação não encontrada.")
        else:
            print("O código deve ser um número inteiro.")

    # Opção 5: Excluir
    elif opcao == 5:
        entrada_codigo = input("Digite o código da manifestação que deseja excluir: ")
        if entrada_codigo.isdigit():
            codigo = int(entrada_codigo)
            linhas = excluirManifestacao(conexao, codigo)
            
            if linhas > 0:
                print("Manifestação excluída com sucesso!")
            else:
                print("Nenhuma manifestação foi excluída (verifique o código).")
        else:
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
