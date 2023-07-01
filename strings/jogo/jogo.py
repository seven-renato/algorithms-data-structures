def abrir_arquivo(nome):
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))      
    arq = open(f"{dir_path}\\{nome}.csv")
    lista = arq.readlines()
    linhas = []
    array = []
    for vet in lista:
        linhas.append(vet[:-1])
    for vetor in linhas:
        array.append(vetor.split(";"))
    return(array)

def jogo(nome):
    import random as rd
    arq = abrir_arquivo("planilha")
    animais = []
    for i in range(len(arq)):
        animais.append(arq[i][0])
    dicas = []
    dica = []
    for vet in arq:
        for i in range(1, len(vet)):
            dica.append(vet[i])
        dicas.append(dica)
        dica = []
    escolha = rd.randint(1, len(animais)-1)
    animal = animais[escolha]
    print(animal, dicas[escolha])
    resposta = ""
    tentativas = 0
    resposta = input("Digite o animal que você acha que é: ").lower()
    while resposta != (animal.lower()):
        tentativas += 1
        if tentativas % 6 == 0:
            desistir = input("Quer desistir, digite sim ou não? ").lower()
            if desistir == "sim":
                print("Você desistiu ;(")
                pontuação = 0
                print("Sua pontuação foi de",pontuação)
                return nome+";"+str(pontuação)
        if tentativas == 3:
            print(dicas[escolha][0])
        if tentativas == 7:
            print(dicas[escolha][1])
        if tentativas == 10:
            print(dicas[escolha][2])
        if tentativas == 15:
            print(dicas[escolha][3])
        print(f"Você fez {tentativas} tentativas.")
        resposta = input("Digite o animal que você acha que é: ").lower()

    pontos = 1000
    pontuação = pontos - (tentativas*10)

    if resposta == (animal.lower()):
        print("Você acertou o animal era", animal)
        print("Sua pontuação foi de",pontuação)
        return nome+";"+str(pontuação)
    print("Você errou o animal era", animal)
    print("Sua pontuação foi de",pontuação)
    return nome+";"+str(pontuação)

def pontuacao():
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))      
    lista.sort(key=lambda x: (x[1]), reverse= True)
    podio = "\n".join(lista)
    nome_do_arq = "pontuacao"
    arq = open(f"{dir_path}\\{nome_do_arq}.csv","w")
    arq.write("Nome;Pontuacao;Posicao\n")
    arq.write(podio)
    arq.close

jogar = "sim"
lista = []
cont = 1
while True:
    nome = input("Digite seu nome: ")
    x = jogo(nome)+";"+str(cont)+'°'
    lista.append(x) 
    cont += 1
    jogar = input("Deseja jogar novamente? ").lower()
    if jogar in ["não", "n", "no"]:
        break
pontuacao()
    
