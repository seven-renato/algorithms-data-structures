import random
def uppercase(string):
    if ord(string) >= 97 and ord(string) <= 122:
        x = ord(string) - 32
        return chr(x)
    else:
        return string
arquivo = open(
    "C:\\Users\\seven\\Documents\\Projetos\\FURG\AULA\\algortimo\\strings\\questao5.txt", "r")
infos = arquivo.readlines()
arquivo.close()

nova_lista = []
for linha in infos:
    nova_lista.append(linha[0:-1])

palavra = random.choice(nova_lista)
lista = list(palavra)
lista[0] = uppercase(lista[0])

random.shuffle(lista)
shuffle_word = "".join(lista)
while shuffle_word == palavra:
    list(shuffle_word)
    shuffle_word = "".join(random.shuffle(shuffle_word))
tentativa = 6
resposta = True
print("Acerte qual é essa palavra que está embaralhada:",shuffle_word)
while resposta != palavra:
    resposta = input("Digite a palavra: ").lower()
    tentativa -= 1
    if tentativa == 0:
        break
    elif resposta != palavra:
        print(f'Você errou, possui mais {tentativa} tentativas')
    if tentativa == 2:
        print("\nNote que a primeira letra está em maiúsculo.")

if tentativa == 0:
    print("Voce perdeu, parabéns!, a palavra era:",palavra)
else:
    print("Você ganhou, parabéns!, a palavra era:",palavra)
