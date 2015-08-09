'''
Created on Jan 7, 2015

@author: sikarwv
'''

import turtle


myTurtle = turtle.Turtle()
myWin = turtle.Screen()

myWin.bgcolor("black")

#myTurtle.clear()
#myTurtle.reset()
myTurtle.penup()
myTurtle.hideturtle()
myTurtle.color("white")

matrix = []
size = 30
offset = 10

def getNeighbors(x, y):
    lst = []
    lst.append([x,y-1])
    lst.append([x,y+1])
    lst.append([x-1,y+1])
    lst.append([x-1,y])
    lst.append([x-1,y-1])
    lst.append([x+1,y+1])
    lst.append([x+1,y])
    lst.append([x+1,y-1])
    return lst

def getPos(index):
    return [index/size, index%size]

def drawScene(myTurtle, matrix, offset):
    for i in range(size * size):
        lst = getPos(i)
        tx = (lst[0] - size/2) * offset
        ty = (lst[1] - size/2) * offset
        myTurtle.goto(tx,ty)
        if matrix[lst[0]][lst[1]] == 1 :
            myTurtle.color("white")
            myTurtle.dot(5)
        else:
            myTurtle.color("black")
            myTurtle.dot(5)
            
def drawGOL(lst, value):
    tx = (lst[0] - size/2) * offset
    ty = (lst[1] - size/2) * offset
    myTurtle.goto(tx,ty)
    if value == 1 :
        myTurtle.color("white")
        myTurtle.dot(5)
    else:
        myTurtle.color("black")
        myTurtle.dot(5)
        
def gameOfLife(matrix, size):
    newMat = createNewMatrix(size)
    for i in range(size * size):
        lst = getPos(i)
        neighbor = getNeighbors(lst[0], lst[1])
        live = getLiveNeighbor(neighbor, size, matrix)
        if matrix[lst[0]][lst[1]] == 1:
            if live==2 or live ==3:
                newMat[lst[0]][lst[1]] = 1
                drawGOL(lst, 1)
            else:
                drawGOL(lst, 0)
        else:
            if live == 3 :
                newMat[lst[0]][lst[1]] = 1
                drawGOL(lst, 1)
                
    return newMat
    

def createNewMatrix(size):
    newMatrix = []
    for i in range(size):
        lst = []
        for j in range(size):
            lst.append(0)
        newMatrix.append(lst)
    return newMatrix


def getLiveNeighbor(neighbors,size,matrix):
    count = 0
    for i in neighbors:
        if ((not i[0] < 0) and (not i[1] < 0)) and ((not i[0] >= size) and (not i[1] >= size)) :
            if matrix[i[0]][i[1]] == 1:
                count = count + 1
    return count

def drawinitshape(matrix):
    #Blinker
    matrix[4][2] = 1
    matrix[5][2] = 1
    matrix[6][2] = 1
    
    matrix[3][8] = 1
    matrix[4][8] = 1
    matrix[4][7] = 1
    matrix[5][7] = 1
    matrix[5][6] = 1
    matrix[6][7] = 1
    matrix[6][8] = 1
    matrix[7][8] = 1


def animate(matrix, myTurtle, offset):
    mat = createNewMatrix(size)
    drawinitshape(mat)
    drawScene(myTurtle, mat, offset)
    while(True):
        mat = gameOfLife(mat, size)
        #drawScene(myTurtle, mat, offset)
        
def printMatrix(matrix):
    for i in matrix:
            print i
    
#drawScene(myTurtle, matrix, offset)
animate(createNewMatrix(size), myTurtle, offset)
myWin.exitonclick() 


