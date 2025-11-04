acao = 0
inventario = []

while True:

    acao = int(input("\nSelecione uma Opção:\n1 - Adiconar Itens ao inventário\n2 - Remover itens do inventário\n3 - Listar todos os itens do iventário\n4 - sair\n"))
    
    if acao == 4:
        break
    elif acao == 1:
        item = input("Digite o nome do item a ser adicionado:")
        inventario.append(item)
        print("Item adicionado com sucesso")
    elif acao == 2:
        item = input("Digite o nome do item que você quer remover? ")
        if item in inventario:
            inventario.remove(item)
            print("item removido com sucesso")
        else:
            print("Erro: Esse item não está no inventario")
    elif acao == 3:
        if len(inventario) == 0:
            print("Inventario vazio")
        else:
            print("--- seu Inventário ---")
            for item in inventario:
                print(item)
            print("-------------------------")
    
