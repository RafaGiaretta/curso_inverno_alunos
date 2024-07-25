vida = 10
moedas = 450
sorte = 0
guerreiro = input("Vamos começar a nossa aventura! Qual seu nome, guerreiro?          ")

print(f"O guerreiro {guerreiro} acordou numa pequena bifurcação, com um único objetivo: chegar ao castelo")
caminho = input("Qual caminho deveriamos seguir? -- [1] Esquerda -- [2] Direita \n")

if caminho == '1':
    cont = 'S'
    print("\n" * 20)
    print("\nVocê encontra um mercador de poções!")
    print("-Bem vindo a minha loja, guerreiro!  Murmura o homem.")
    print("-Meus preços são... irresistiveis!")
    while cont == 'S':
        print("\n\n\n----------Itens----------")
        print("[1] Espada dupla  --  $250")
        print("[2] Poção de vida  --  $50")
        print("[3] Amuleto da sorte  --  $450")
        print("[4] Credo, não compro com bandeirantes!")

        escolha = input("Escolha um item: \n")
        if escolha == '1':
            moedas -= 250
            print("\n"*20)
            print("\n -Hphm... tão previsível...")
            print(f"\n (ainda restam {moedas} moedas)")
        if escolha == '2':
            moedas -= 50
            print("\n"*20)
            print("\n -Essa é a que mais sai! Não tome com estomago vazio. \n Estou falando sério!")
            print(f"\n (ainda restam {moedas} moedas)")
        if escolha == '3':
            if sorte == 1:
                print("-SEM MAIS AMULETOS!")
            else:
                print("\n"*20)
                print("\n -Hahahaha! Espero que isso te ajude...HAHAHAHAHA")
                print("\n O mercador se perde rindo... Ele não te cobrou... Mas seria rude interromper")
                print(f"\n (ainda restam {moedas} moedas)")
                sorte += 1
        if escolha == '4':
            print("\n"*20)
            print("Em todos esses anos nunca fui tão ofendido! Saia daqui!")
            cont = "idiota"
        print("\n\n\n-Gostaria de comprar algo mais?")
        print("[S]    [N]")
        cont = input("\n").upper()

else:
    print("\n" * 20)
    print("Você encontra uma pequena gosma... quase sem forças... deve ser um alvo fácil!")
    print("----------Combate----------")
    print("[1] Você chuta ela! (que maldade...)")
    print("[2] Você joga uma pedra nela! Ou um galho, alguma coisa")
    print("[3] Você fica parado""\033[3m de forma ameaçadora\033[0m")
    escolha = input("Qual ação você tomará?")
    match escolha:
        case '1':
            print("\n" *20)
            print("Ela gruda no seu pé, sugando sua energia vital!")
            print("Que nojo...")
            print("Mas que ideia também?")
            vida -= 1
            sorte += 1
            print("\n\n\n Mas ela parece estar melhor... fico feliz por ela")
            print(f"O {guerreiro} ainda tem {vida} de vida restante")
        case '2':
            print("\n" *20)
            print("Você arremesa uma pedra nela! E um galho! E um tronco! E... uma galinha?")
            print("Ela parece ter absorvido tudo...")
            print("Só eu que não entendo a anatomia desses bichos?")
            print("Ela... parece estar indo embora, contente!")
            print("Parece que a digestão dela deixou um machado para você!")
            print("\n Ele está um pouco gosmento... e tem resto de galinha nele...")
            print("\033[3mVocê obteve um machado nojento!\033[0m")
        case '3':
            print("\n"*20)
            print("Vocês se encaram...")
            print("Ela... morre?")
            print("...")
            print("Parece que sim, melhor esperar pra ter certeza")
            print("É... ela morreu")
            print("\033[3mVocê recebe o resto mortal de uma slime!\033[0m")
        case _:
            print("\n\n")
            print("melhor deixar ela por si só...")

print("\n\n cabou =) ")

        
    



