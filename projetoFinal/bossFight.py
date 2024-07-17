import random

vida_boss = 100
vida_guerreiro = 100
usos_magia = 3
usos_cura = 3
vida_maxima_guerreiro = 100

def boss_ataque():
    global vida_boss
    ataque_mordida = random.randint(10, 20)
    ataque_unha_sangrenta = random.randint(15, 25)
    ataque_critico = random.randint(30, 40)
    
    if vida_boss <= 25 and random.random() < 0.3: 
        dano = ataque_critico
        tipo_ataque = "degolador"
    else:
        if random.choice([True, False]):  # Aqui troca de ataque normal e os de magia
            dano = ataque_mordida
            tipo_ataque = "mordida"
        else:
            dano = ataque_unha_sangrenta
            tipo_ataque = "com suas unhas rasgantes"

    if vida_boss <= 10:
        frase = "O boss está furioso: 'Eu não vou ser derrotado!'"
    elif vida_boss <= 45:
        frase = "O boss grita: 'Você não vai escapar tão facilmente!'"
    elif vida_boss <= 75:
        frase = "O boss ruge: 'Você é forte, mas eu sou mais forte!'"
    else:
        frase = ""

    return tipo_ataque, dano, frase

def guerreiro_ataque():
    global vida_guerreiro, vida_boss, usos_magia, usos_cura
    
    def atacar():
        return random.randint(10, 20)

    def curar():
        cura = random.randint(15, 25)
        return min(vida_maxima_guerreiro, vida_guerreiro + cura)

    def soltar_magia():
        return random.randint(20, 30)
    
    print(f"\nVida do boss: {vida_boss}")
    print(f"Vida do guerreiro: {vida_guerreiro}")
    print(f"Magias restantes: {usos_magia}")
    print(f"Curas restantes: {usos_cura}\n")
    
    acao = input("Escolha uma ação (atacar, curar, magia): ").lower()
    
    match acao:
        case "atacar":
            dano = atacar()
            vida_boss -= dano
            print(f"Você atacou o boss e causou {dano} de dano!")
        
        case "curar" if usos_cura > 0:
            vida_guerreiro = curar()
            usos_cura -= 1
            print(f"Você se curou! Sua vida agora é {vida_guerreiro}. Curas restantes: {usos_cura}.")
        
        case "curar":
            print("Você não tem mais poção de cura no estoque!")
        
        case "magia" if usos_magia > 0:
            dano = soltar_magia()
            vida_boss -= dano
            usos_magia -= 1
            print(f"Você usou poção de magia e causou {dano} de dano! Poções mágicas restantes: {usos_magia}")
        
        case "magia":
            print("Você não tem mais poções de magia!")
        
        case _:
            print("O guerreiro não conhece esse movimento. Tente novamente.")
            return False  
        
    return True  

def main():
    global vida_guerreiro, vida_boss
    print("\nEnquanto o guerreiro seguia sua jornada, percorrendo a floresta escura, encontrou um monstro de olhos verdes, pelos escuros, dentes amarelos e de tamanho de uma árvore.\nO monstro se preparou para um ataque, e o guerreiro sacou sua espada...")
    print("\nPrepare-se para o combate, monstro!")
    print("Inciando combate:")
    while vida_boss > 0 and vida_guerreiro > 0:
        acao_valida = guerreiro_ataque()
        if not acao_valida:
            continue  

        if vida_boss <= 0:
            print("\nO monstro foi derrotado!\nVocê venceu!!!")
            break

        tipo_ataque_boss, dano_boss, frase_boss = boss_ataque()
        vida_guerreiro -= dano_boss
        vida_guerreiro = max(0, vida_guerreiro)  
        print(f"O monstro realizou um ataque {tipo_ataque_boss} causando {dano_boss} de dano.")
        if frase_boss:
            print(frase_boss)
        print(f"Vida do guerreiro: {vida_guerreiro}\n")
        
        if vida_guerreiro <= 0:
            print("\nVocê foi derrotado!\nO monstro venceu.")
            break

if __name__ == "__main__":
    main()
