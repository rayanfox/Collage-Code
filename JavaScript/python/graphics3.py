from graphics import * 
import os
import tkinter

def main():
    win = GraphWin('tri',500,500)
    win.setBackground('gray')
    
  
    p1=win.getMouse()
    p1.draw(win)   
    p2=win.getMouse()
    p2.draw(win)   
    p3=win.getMouse()
    p3.draw(win)
    
    points=[p1,p2,p3]

    tri = Polygon(points)
    tri.setFill('gray')
    tri.setOutline('cyan')
    tri.setWith(4)
    tri.draw(win)

main()    
      

