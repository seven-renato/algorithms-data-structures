arquivo = open("notas.txt", "w")
numNotas = 2 
numAlunos = 5
minhastring = ""

for aluno in range(numAlunos):
    nome = input("Informe o nome do aluno: ")
    soma = 0
    for nota in range(numNotas):
        valor = float(input("Digite uma nota: "))
        minhastring += str(valor)+"-"
        soma += valor
    media = soma / numNotas
    minhastring += str(media)+"\n"
    arquivo.write(minhastring)
arquivo.close()