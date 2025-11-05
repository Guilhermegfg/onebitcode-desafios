
lutador1= {}
lutador2= {}
turno = 0

print("Bem vindo ao Mestre dos Duelos RPG!!!\nDigite as informações do lutador 1!!! ")

lutador1["nome"] = input("Digite o nome do lutador1: ")
lutador1["classe"] = input(f"digite a classe do {lutador1['nome']}: ")
lutador1["vida"] = int(input(f"digite a vida do {lutador1['nome']}: "))
lutador1["poder"] = int(input(f"digite a poder do {lutador1['nome']}: "))

print("Agora vamos definir o lutador2")

lutador2["nome"] = input("Digite o nome do lutador2: ")
lutador2["classe"] = input(f"digite a classe do {lutador2['nome']}: ")
lutador2["vida"] = int(input(f"digite a vida do {lutador2['nome']}: "))
lutador2["poder"] = int(input(f"digite a poder do {lutador2['nome']}: "))



def duelo (lutador1, lutador2):
    turno = 0
    while lutador1["vida"] >0 and lutador2["vida"] > 0:
        if turno % 2 == 0:
            lutador2["vida"] -= lutador1["poder"]
            print(lutador2["vida"])
        else:
            lutador1["vida"] -= lutador2["poder"]
            print(lutador1["vida"])
        turno += 1

    if lutador1["vida"] > lutador2["vida"]:
        print(f"O {lutador1["nome"] } é o vencedor")
    else:
        print(f"O {lutador2["nome"]} é o vencedor")

duelo(lutador1, lutador2)