import graphics as gf
from graphics import *
import math

from time import sleep

win = gf.GraphWin("Relógio", 1200, 700)


def criarRelogio(win, raio):
    centro = gf.Point(600, 350)
    voltaRelogio = gf.Circle(centro, raio+50)
    voltaRelogio.setFill("red")
    voltaRelogio.draw(win)
    relogio = gf.Circle(centro, raio)
    relogio.setFill("white")
    relogio.draw(win)
    pontoDoMeio = gf.Circle(centro, 8)
    pontoDoMeio.setFill("red")
    pontoDoMeio.draw(win)
    angulo = 90
    for i in range(12):
        ptFinal = gf.Point(centro.getX()-(raio-30)*math.cos(angulo*math.pi/180),
                           centro.getY()-(raio-30)*math.sin(angulo*math.pi/180))
        if i == 0:
            num = gf.Text(ptFinal, 12)
            num.setSize(20)
            num.draw(win)
        else:
            num = gf.Text(ptFinal, i)
            num.setSize(20)
            num.draw(win)
        angulo += 30
    anguloMin = 90
    # for i in range(60):
    #     ptFinalMin = gf.Point(centro.getX()-(raio-30)*math.cos(angulo*math.pi/180),
    #                           centro.getY()-(raio-30)*math.sin(angulo*math.pi/180))
    #     if anguloMin % 90 == 0:
    #         pass
    #     else:
    #         linha = gf.Line(centro, ptFinalMin)
    #         linha.draw(win)
    #     anguloMin += 6
    #     pass


def girarSec(win, angulo, centro, raio):
    ptFinal = gf.Point(centro.getX()-(raio-180)*math.cos(angulo*math.pi/180),
                       centro.getY()-(raio-180)*math.sin(angulo*math.pi/180))
    linha = gf.Line(centro, ptFinal)
    linha.draw(win)
    time.sleep(1)
    linha.undraw()
    return angulo


def girarRelogio(win, hora, minu, sec, raio):
    centro = gf.Point(600, 350)
    sec = sec % 60
    minu = minu % 60
    hora = hora % 24
    cont = sec
    cont2 = minu
    anguloSec = 90 + (6*sec)
    anguloMin = 90 + (6*minu)
    anguloHora = 90 + (30*hora) + (0.5*minu)
    ptFinalMin = gf.Point(centro.getX()-(raio-100)*math.cos(anguloMin*math.pi/180),
                          centro.getY()-(raio-100)*math.sin(anguloMin*math.pi/180))
    linhaMin = gf.Line(centro, ptFinalMin)
    linhaMin.draw(win)
    ptFinalHora = gf.Point(centro.getX()-(raio-30)*math.cos(anguloHora*math.pi/180),
                           centro.getY()-(raio-30)*math.sin(anguloHora*math.pi/180))
    linhaHora = gf.Line(centro, ptFinalHora)
    linhaHora.draw(win)
    while True:
        girarSec(win, anguloSec, centro, raio)
        if cont % 6 == 0:
            linhaMin.undraw()
            ptFinalMin = gf.Point(centro.getX()-(raio-100)*math.cos(anguloMin*math.pi/180),
                                  centro.getY()-(raio-100)*math.sin(anguloMin*math.pi/180))
            linhaMin = gf.Line(centro, ptFinalMin)
            linhaMin.draw(win)
            anguloMin += 0.6
            cont2 += 1
            if cont2 % 6 == 0:
                linhaHora.undraw()
                ptFinalHora = gf.Point(centro.getX()-(raio-30)*math.cos(
                    anguloHora*math.pi/180), centro.getY()-(raio-30)*math.sin(anguloHora*math.pi/180))
                linhaHora = gf.Line(centro, ptFinalHora)
                linhaHora.draw(win)
                anguloHora += 0.3
                cont2 += 1
            if cont % 3600 == 0:
                print("Passei")
                print(cont)
        anguloSec += 6
        cont += 1


raio = 300
criarRelogio(win, raio)
girarRelogio(win, 11, 60, 57, raio)
cliquei = win.getMouse()
win.close()
