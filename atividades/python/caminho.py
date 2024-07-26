guerreiro = input("Qual o nome do guerreiro? ")

print(f"Enquanto o guerreiro {guerreiro} seguia seu caminho, entrou em um empasse")

def condicao():
    resposta = 'S'
    moedas = 450.0

    while resposta == 'S' and moedas > 0:
            escolha = input("Escolha um item: \n")

            if escolha == '1':
                moedas -= 250.0
                print(f"Ainda restam {moedas}")
            elif escolha == '2':
                moedas -= 150.0
                print(f"Ainda restam {moedas}")
            else:
                moedas -= 300.0
                print(f"Ainda restam {moedas}") 

            resposta = input("Deseja continuar comprando? [S] ou [N]").upper() 

def menu():
    print("Voce encontrou um mercador de pocoes")
    print("Bem vindo ao mercador de pocoes")
    print("*******Itens*********\n")
    print("Item 1: Espada dupla -- preco 250.0")
    print("Item 2: pocao de vida -- preco 150")
    print("Item 3: pocao de magia -- preco 300")

def direita():
    print(f"O guerreiro {guerreiro} escolheu a direita, e vai seguir colhendo material")

def caminho ():        

    caminho = input("Escolha uma lado -- [1] esquerda -- [2] direita \n")

    if caminho == '1':
        menu()
        condicao()          
    else:
        direita()    

caminho()