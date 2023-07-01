import graphics as gf
from graphics import *
width = 1300
height = 600

win = gf.GraphWin("Jogo da forca", width, height)


def desenhaForca(win):
    vet = []

    base = gf.Line(gf.Point(100, 300), gf.Point(150, 300))
    base.draw(win)
    vet.append(base)

    lineUp = gf.Line(gf.Point(125, 300), gf.Point(125, 170))
    lineUp.draw(win)
    vet.append(lineUp)

    lineHoriz = gf.Line(gf.Point(125, 170), gf.Point(225, 170))
    lineHoriz.draw(win)
    vet.append(lineHoriz)

    lineToDown = gf.Line(gf.Point(225, 170), gf.Point(225, 200))
    lineToDown.draw(win)
    vet.append(lineToDown)

    lineTraco = gf.Line(gf.Point(200, 200), gf.Point(250, 200))
    lineTraco.draw(win)
    vet.append(lineTraco)

    return vet


def desenhaBaseLet(win, len):
    vet = []
    for i in range(len):
        let = gf.Line(gf.Point(260+(i*40), 300), gf.Point(290+(i*40), 300))
        let.draw(win)
        vet.append(len)
    return vet


def desenhaBoneco(boole, cont, win):
    if boole and cont == 1:
        c = gf.Circle(gf.Point(225, 210), 10)
        c.draw(win)
    elif boole and cont == 2:
        b = gf.Line(gf.Point(225, 220), gf.Point(225, 260))
        b.draw(win)
    elif boole and cont == 3:
        rH = gf.Line(gf.Point(225, 230), gf.Point(245, 240))
        rH.draw(win)
    elif boole and cont == 4:
        lH = gf.Line(gf.Point(225, 230), gf.Point(205, 240))
        lH.draw(win)
    elif boole and cont == 5:
        rF = gf.Line(gf.Point(225, 260), gf.Point(245, 275))
        rF.draw(win)
    elif boole and cont == 6:
        lF = gf.Line(gf.Point(225, 260), gf.Point(205, 275))
        lF.draw(win)
    elif boole and cont == 7:
        rightEye = gf.Circle(gf.Point(230, 208), 2)
        rightEye.draw(win)
    elif boole and cont == 8:
        leftEye = gf.Circle(gf.Point(220, 208), 2)
        leftEye.draw(win)
    elif boole and cont == 9:
        mouth = gf.Line(gf.Point(220, 215), gf.Point(230, 215))
        mouth.draw(win)


def letraCerta(string, palavra):
    vet = []
    cont = 0
    if string in palavra:
        for letter in palavra:
            if letter == string:
                vet.append(cont)
            cont += 1
    else:
        return False
    return vet

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto = list(alfabeto)
desenhaForca(win)
n = 6

ganhou = False
cont = 0
k = 0
x = 280
let = 275
usadas = []
palavra = input().upper()
# palavra = "ACARAJE"
if len(palavra) > 6:
    n = 9
desenhaBaseLet(win, len(palavra))
while True:
    # print(k)
    # print(cont)
    if k == len(palavra):
        ganhou = True
        break
    if cont == n:
        time.sleep(1.5)
        imag = Image(Point(
            500, 300), "/home/aluno/Área de Trabalho/Graphics-20220928T110828Z-001/Graphics/src/122-1211555_sangre-cartoon-blood-splatter-png.gif")
        imag.draw(win)
        break
    letter = win.getKey().upper()
    while letter in usadas or letter not in alfabeto:
        letter = win.getKey().upper()
    usadas.append(letter)
    # print(usadas)
    if letraCerta(letter, palavra):
        for val in letraCerta(letter, palavra):
            letter1 = gf.Text(gf.Point(let+(40*val), 285), letter)
            letter1.setSize(20)
            letter1.draw(win)
            k += 1
    else:
        cont += 1
        desenhaBoneco(True, cont, win)
        x += 30
        letraErrada = gf.Text(gf.Point(x, 220), letter)
        letraErrada.draw(win)

time.sleep(3)
c = gf.Circle(gf.Point(10, 20), 7000)
c.setFill("white")
c.draw(win)
if ganhou:
    congr = gf.Text(gf.Point(400, 300), "Parabéns! Você acertou!")
    congr.setSize(30)
    congr.draw(win)
    img = Image(Point(
        900, 300), "/home/aluno/Área de Trabalho/Graphics-20220928T110828Z-001/Graphics/src/GUNzxe2b_400x401.gif")
    img.draw(win)
else:
    congr = gf.Text(gf.Point(250, 300),
                    f"Whoops... Você errou!\n A palavra era: '{palavra}'")
    congr.setSize(30)
    congr.draw(win)
    img = Image(Point(
        900, 300), "/home/aluno/Área de Trabalho/Graphics-20220928T110828Z-001/Graphics/src/FOY_l23XwAgYutd.gif")
    img.draw(win)

cliquei = win.getMouse()
win.close()
