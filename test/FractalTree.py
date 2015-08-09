'''
Created on Jan 7, 2015

@author: sikarwv
'''
import turtle


myTurtle = turtle.Turtle()
myWin = turtle.Screen()

myWin.bgcolor("lightgreen")

myTurtle.penup()
#myTurtle.setpos(-100, 100)
#myTurtle.pendown()
#myTurtle.forward(100)
myTurtle.shape("turtle")
myTurtle.color("blue")

def drawTess(myTurtle, s):
    size = 5
    for i in range(s):
        #myTurtle.stamp()
        size = size + 1
        myTurtle.dot(2)
        myTurtle.forward(size)
        myTurtle.right(24)

def drawSprial(myTurtle, linlen):
    if linlen > 0:
        myTurtle.forward(linlen)
        myTurtle.right(90)
        drawSprial(myTurtle, linlen-5)
        
#drawSprial(myTurtle, 500)

drawTess(myTurtle, 50)

myWin.exitonclick() 