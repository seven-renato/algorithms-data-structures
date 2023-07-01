from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input("Digite a sua jogada: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
print("-="*11)
print("- Computador jogou {}".format(itens[computador]))
print("- Jogador jogou {}".format(itens[jogador]))
print("-="*11)
if computador == jogador:
    print("Deu Empate!")
if computador == 0:
    if jogador == 1:
        print("O jogador venceu!")
    elif jogador ==2:
        print("O computador venceu!")
elif computador == 1:
    if jogador == 2:
        print("O jogador venceu!")
    elif jogador == 0:
        print("O computador venceu!")
elif computador == 2:
    if jogador == 0 :
        print("O jogador venceu!")
    elif jogador == 1:
        print("O computador venceu!")
