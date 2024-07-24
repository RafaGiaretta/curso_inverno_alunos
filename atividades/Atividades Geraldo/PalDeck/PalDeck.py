nome = input ("Digite seu nome: ")
print (f"Pal dex de {nome}")

quantidade_pal = int (input ("Quantos pals você tem: "))
print (f"{nome} possuiu {quantidade_pal} pals")

inserir = int (input ("Quantos pals novos você capturou: "))

nova_quantidade = quantidade_pal + inserir

print (f"{nome} capturou {inserir}! Agora tem {nova_quantidade}")