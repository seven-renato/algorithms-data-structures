import random
#import tkinter as tk
import graphics as gf

"""root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()"""

width = 500
height = 500


win = gf.GraphWin("Minha Janela",width,height)
c = gf.Circle(gf.Point(50,50),10)
c.draw(win)
random.seed()

"""cont = 0
while True:
    cliquei = win.getMouse()#retorna a posição onde foi clickado, em forma de variável
    if cliquei:
        cont += 1
        print(cont)
    cliquei = False
"""
while True:
    forms = ["Circle","Rectangle","Polygon"]
    formChoose = forms[random.randint(0,len(forms)-1)]  

    red, green, blue = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    cliquei = win.getMouse()
    if formChoose == "Circle":
        nova_forma = gf.Circle(cliquei,random.randint(0,255),)
    elif formChoose == "Rectangle":
        nova_forma = gf.Rectangle(cliquei,random.randint(0,255),)
    else:
        nova_forma = gf.Polygon(cliquei,random.randint(0,255),)
    nova_forma.setFill(gf.color_rgb(red, green, blue))
    nova_forma.draw(win)

win.close


"""cliquei = win.getMouse()
while True:
    tecla = win.checkKey()

    if tecla == "KP_4":
        c.move(-2,0)
    elif tecla == "KP_8":
        c.move(0,-2)
    elif tecla == "KP_2":
        c.move(0,+2)
    elif tecla == "KP_6":
        c.move(+2,0)
    elif tecla == "KP_7":
        c.move(-2,-2)
    elif tecla == "KP_9":
        c.move(+2,-2)
    elif tecla == "KP_1":
        c.move(-2,+2)
    elif tecla == "KP_3":
        c.move(+2,+2) 
    #c.move(random.randint(-10,10),random.randint(-10,10))"""









win.close()