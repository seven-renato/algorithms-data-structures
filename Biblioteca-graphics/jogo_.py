import graphics as gf
import random
width = 500
height = 500

win = gf.GraphWin("Minha Janela", width, height)
c = gf.Circle(gf.Point(50, 50), 10)
c.draw(win)
random.seed()
caixa = gf.Rectangle(gf.Point(150, 150), gf.Point(150, 250))
caixa.draw(win)


cliquei = win.getMouse()

r = 0
g = 0
b = 0
while True:
    c.setFill(gf.color_rgb(r, g, b))
    tecla = win.checkKey()
    if tecla == "Left":
        c.move(-5, 0)
    elif tecla == "Up":
        c.move(0, -5)
    elif tecla == "Down":
        c.move(0, +5)
    elif tecla == "Right":
        c.move(+5, 0)
    center = c.getCenter()
    xPos = center.getX()
    tryX = xPos + c.getRadius()
    yPos = center.getY()
    tryY = yPos + c.getRadius()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    if tryX in range(150, 171) and (tryY in range(150,271)):
        win.close()
