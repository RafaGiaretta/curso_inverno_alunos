moedas = 250.0

guerreiro = input ("Qual o nome do guerreiro? \nResposta: ")

def direita () :
    print (f"\nO guerreiro {guerreiro} seguiu pela direita e não encontrou nada na sua jornada.")

def esquerda () :
    print (f"\nO guerreiro {guerreiro} seguiu pela esquerda e encontrou um mercador de poções.")
    
    mercador(moedas)

def mercador (moedas) :
    print ("\n~~ Ola estranho, tenhos algumas coisas raras para vender! ~~ Disse o mercador abrindo sua jaqueta e mostrando seus itens.")
    print ("\n********** Itens ***********")
    print ("Item 1: Espada dupla -- preço $ 250.00")
    print ("Item 2: Poção de vida -- preço $ 150.00")
    print ("Item 3: Poção de mana -- preço $ 300.00")

    comprar = int (input (f"\nO guerreiro {guerreiro} possui {moedas} moedas, ele vai comprar algum item? \n[1] Sim   [2] Não \nResposta: "))

    if comprar == 1 :
        while comprar == 1:
            item = int (input ("\nEscolha um item da loja: \n[1] Espada dupla   [2] Poção de vida   [3] Poção de mana\nResposta:"))

            if item == 1 :
                if moedas < 250.0 :
                    print (f"\nO guerreiro {guerreiro} não possuí moedas suficiente para comprar a espada, seu saldo atual é de {moedas} moedas.")

                else :
                    moedas -= 250.0
                    print (f"\nO guerreiro {guerreiro} comprou uma Espada dupla e agora possui {moedas} moedas.")
            
            elif item == 2 : 
                if moedas < 150.0 :
                    print (f"\nO guerreiro {guerreiro} não possuí moedas suficiente para comprar a poção, seu saldo atual é de {moedas} moedas.")

                else :
                    moedas -= 150.0
                    print (f"\nO guerreiro {guerreiro} comprou uma Poção de vida e agora possui {moedas} moedas.")

            else :
                if moedas < 300.0 :
                    print (f"\nO guerreiro {guerreiro} não possuí moedas suficiente para comprar a poção, seu saldo atual é de {moedas} moedas.")

                else :
                    moedas -= 300.0
                    print (f"\nO guerreiro {guerreiro} comprou uma Poção de vida e agora possui {moedas} moedas.")
                    
            comprar = int (input (f"\nO guerreiro {guerreiro} quer comprar outro item? \n[1] Sim   [2] Não \nResposta: "))
        print (f"\nO guerreiro {guerreiro} seguiu sua jornada.") 
    else :
        print (f"\nO guerreiro {guerreiro} não compra nada na loja.")

def main () :
    print (f"\nEnquanto o guerreiro {guerreiro} seguia sua jornada, ele se depara com uma bifurcação.")
    print (f"Olhando para a esquerda ele avista uma figura misteriosas.")
    print ("Já olhando para a direita ele não encherga nada suspeito.")
    caminho = int (input ("Qual caminho ele vai seguir? \n[1] Esquerda   [2] Direita \nResposta: "))

    if caminho == 1 :
        esquerda ()

    else :
        direita ()

if __name__ == '__main__' :
    main ()