from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA""")
jogador = int(input("Qual sua jogada? "))
print("PEDRA...")
sleep(0.5)
print("PAPEL...")
sleep(0.5)
print("TESOURA!")

print("-=" * 15)
print(f"Computador jogou {(itens[computador])}")
print(f"Jogador jogou {(itens[jogador])}")
print("-=" * 15)

if computador == 0: #pedra
    if jogador == 0:
        print("EMPATE!")
    
    elif jogador == 1:
        print("Jogador VENCE!")

    elif jogador == 2:
        print("Jogador PERDE!")
    
    else:
        print("Jogada inválida.")

elif computador == 1: #papel
    if jogador == 0:
        print("Jogador PERDE!")
    
    elif jogador == 1:
        print("EMPATE!  ")

    elif jogador == 2:
        print("Jogador VENCE!")
    
    else:
        print("Jogada inválida.")

elif computador == 2: #tesoura
    if jogador == 0:
        print("Jogador VENCE!")
    
    elif jogador == 1:
        print("Jogador PERDE!")

    elif jogador == 2:
        print("EMPATE!")
    
    else:
        print("Jogada inválida.")
else:
        print("Jogada inválida.")
