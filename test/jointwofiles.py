'''
Created on Feb 9, 2015

@author: sikarwv
'''

f = open("inventory_test.txt", "a")

file1 = open("example1.txt", "r")
for line in file1: f.write(line)
file1.close()

file2 = open("example2.txt", "r")
for line in file2: f.write(line)
file2.close()

file3 = open("example3.txt", "r")
for line in file3: f.write(line)
file3.close()

f.close()
