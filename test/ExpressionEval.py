'''
Created on Jan 6, 2015

@author: sikarwv
'''
from Stack import Stack


def infixToPostFix(infixExpr):
    prio = {"^" : 4,
            "*" : 3, 
            "/" : 3,
            "+" : 2,
            "-" : 2,
            "(" : 1}
    
    opStack = Stack()
    
    postFixList = []
    tokenList = infixExpr.split()
    
    for token in tokenList:
        
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token.isdigit():
            postFixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postFixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prio[opStack.peek()] >= prio[token]):
                postFixList.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():
        postFixList.append(opStack.pop())
        
    return " ".join(postFixList)


def evalPostFix(postFixExp):
    tokenList = postFixExp.split()
    opStack = Stack()
    for token in tokenList:
        if token.isdigit():
            opStack.push(token)
        else:
            op2 = opStack.pop()
            op1 = opStack.pop()
            result = calc(op1, op2, token)
            opStack.push(result)
    return opStack.pop()

def calc(o1, o2, token):
    op1 = int(o1)
    op2 = int(o2)
    if token == "*":
        return op1 * op2
    elif token == "/":
        return op1 / op2
    elif token == "+":
        return op1 + op2
    elif token == "^":
        return op1**op2
    else:
        return op1 - op2
    
#print(evalPostFix("7 8 + 3 2 + /"))
#print(evalPostFix("17 10 + 3 * 9 /"))
#print(infixToPostFix("10 + 3 * 5 / ( 16 - 4 )"))
#print(evalPostFix(infixToPostFix("10 + 3 * 5 / ( 16 - 4 )")))
#print(infixToPostFix("A * B + C * D"))
##print(infixToPostFix("( A + B ) * C - ( D - E ) * ( F + G )"))
#print(infixToPostFix("5 * 3 ^ ( 4 - 2 )"))
#print(evalPostFix(infixToPostFix("5 * 3 ^ ( 4 - 2 )")))
#inStr = raw_input("expression : ")
#print(infixToPostFix(inStr))
#print(evalPostFix(inStr))