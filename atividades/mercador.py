guerreiro = 450.0

print("Em sua jornada, nosso guerreiro encontrou um comerciante pelo caminho!\n")
print("Bem-vindo guerreiro! \n Tenho as melhores poções e armaduras\n")
print("**********************************************")
print("1. Espada dupla: 150.0 moedas")
print("2. Ferro sagrado para espada: 75.0 moedas")
print("3. Excalibbur: 400.0 moedas")
print("4. Golden Helmet: 250.0 moedas")
print("5. Poção dano de força: 50.0 moedas")
print("6. Poção dano de corte: 50.0 moedas")
print("7. Poção de vida: 50.0 moedas")
print("8. Armadura: 150.0 moedas")
print("**********************************************")

print(f"Moedas disponiveis: {guerreiro}")
item_escolhido = input("Digite o número do item que você deseja comprar (1-8): ")

match item_escolhido:
    case "1":
        preco_item = 150.0
        nome_item = "Espada dupla"
    case "2":
        preco_item = 75.0
        nome_item = "Ferro sagrado para espada"
    case "3":
        preco_item = 400.0
        nome_item = "Excalibur"
    case "4":
        preco_item = 250.0
        nome_item = "Golden Helmet"
    case "5":
        preco_item = 50.0
        nome_item = "Poção dano de força"
    case "6":
        preco_item = 50.0
        nome_item = "Poção dano de corte"
    case "7":
        preco_item = 50.0
        nome_item = "Poção de vida"
    case "8":
        preco_item = 150.0
        nome_item = "Armadura"
    case _:
        preco_item = 0.0
        nome_item = ""
        print("Item inválido!")

if preco_item > 0:
    quantidade = int(input(f"Quantas unidades de {nome_item} você deseja comprar? "))
    custo_total = preco_item * quantidade
    
    if custo_total <= guerreiro:
        guerreiro -= custo_total
        print(f"Você comprou {quantidade} unidades de {nome_item} por {custo_total} moedas.")
        print(f"Moedas restantes do guerreiro: {guerreiro}")
    else:
        print("Você não tem moedas suficientes.")

print("Boa sorte na sua aventura, Guerreiro!")        
