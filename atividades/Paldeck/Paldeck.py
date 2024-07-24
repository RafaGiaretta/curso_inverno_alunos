continua = 1
nome = input("Digite seu nome: ")
qnt = 0
while continua:
    qnt+= 1
    pal = input("Digite o nome do Pal: ")
    print(f"Agora, o pal {pal} é o fiel companheiro de {nome}")
    print(f"Quantidade de Pals: {qnt}")
    continua = int(input("Deseja continuar? (0 = não desejo) "))


    