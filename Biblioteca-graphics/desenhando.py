from graphics import *


def main():
    win = GraphWin("Meu Campo", 200, 140)
    campo = Rectangle(Point(10, 10), Point(190, 130))
    campo.draw(win)
    c = Circle(Point(100, 70), 25)
    c.draw(win)
    meioCampo = Line(Point(100,10),Point(100,130))
    meioCampo.draw(win)

    entrada = Entry(Point(10,10),30)
    entrada.draw(win)
    Texto = entrada.getText()
    print(Texto)








    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
