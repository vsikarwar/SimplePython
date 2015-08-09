'''
Created on Jan 7, 2015

@author: sikarwv
'''
import Tkinter


top = Tkinter.Tk()

w = Tkinter.Canvas(top, width=200, height=100)
w.pack()

for i in range(1000):
    w.create_line(i, i, 200, 100)


w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")
top.mainloop()