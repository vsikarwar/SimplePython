'''
Created on Feb 6, 2015

@author: sikarwv
'''

import random
import string

def getOptionCodes():
    opcode = ''+getRandomString(2)
    for i in range(1000): opcode += " "+getRandomString(2)
    return opcode


def getRandomString(lengthOfString):
    return ''.join(random.choice(string.ascii_uppercase) for i in range(lengthOfString))

def main():
    no_of_line = 5000000
    start = 4000000
    file = open("example5.txt", "w")
    header = []
    header.append("vin\t")
    
    header = ["Vin", "Year", "Make", "Model", "Trim", "Exterior Color", "ExtColorCode", 
              "Interior Color", "Amenities", "MSRP", "Transmission", "Speeds"]
    
    data = {}
    
    #Write header
    head = ""
    for item in header: head += item+"\t"
    
    if start == 0 : file.write(head.strip()+"\n")
    
    #write body
    for i in range(start, no_of_line):
        line = ""
        data["Vin"] = "1AAAA"+str(i)
        data["Year"] = str(random.randint(2001,2020))
        data["Exterior Color"] = getRandomString(256)
        data["ExtColorCode"] = getRandomString(15)
        data["MSRP"] = ''.join(random.choice(string.digits) for i in range(8))
        data["Amenities"] = getOptionCodes()
        data["Interior Color"] = getRandomString(256)
        data["Make"] = getRandomString(32)
        data["Trim"] = getRandomString(32)
        data["Model"] = getRandomString(32)
        data["Transmission"] = getRandomString(10)
        data["Speeds"] = str(random.randint(0,9))
        for item in header: line+= data[item]+"\t"
        file.write(line.strip()+"\n")
        
    file.close()
    
main()
