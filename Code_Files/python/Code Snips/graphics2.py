from graphics import * 
import os
import tkinter

def main():


    win = GraphWin()

    pt = Point(150,50)

    cr = Circle(pt,25)


    cr.setOutline('red')
    cr.setWidth(3)
    cr.setFill('black')

    
    cr.draw(win)
    win.getMouse()


main()

