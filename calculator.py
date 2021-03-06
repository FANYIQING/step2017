# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:13:46 2017

@author: Administrator
"""

def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index



def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiple(line, index):
    token = {'type': 'MULTIPLE'}
    return token, index + 1

def readDivide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1    

def readLeft(line, index):
    token = {'type': 'LEFT'}
    return token, index + 1

def readRight(line, index):
    token = {'type': 'RIGHT'}
    return token, index + 1    

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiple(line, index)
        elif line[index] == '/':
            (token, index) = readDivide(line, index)        
        elif line[index] == '(':
            (token, index) = readLeft(line, index)
        elif line[index] == ')':
            (token, index) = readRight(line, index)        
        else:
            print 'Invalid character found: ' + line[index]
            exit(1)
        tokens.append(token)
    return tokens


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    
    while index < len(tokens):
        if tokens[index]['type'] == 'LEFT':
            r_index = len(tokens)-1
            while index < r_index:
                if tokens[r_index]['type'] == 'RIGHT':
                    tokens[index] = token = {'type': 'NUMBER', 'number': evaluate(tokens[index+1: r_index])}
                    del(tokens[index+1 : r_index+1])
                    break
                r_index -= 1
            break
        index += 1
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLE':
                tokens[index-2]['number'] *= tokens[index]['number']
                del(tokens[index-1:index + 1])
                
                index -= 3
            elif tokens[index - 1]['type'] == 'DIVIDE':
                tokens[index-2]['number'] = float(tokens[index-2]['number']) / tokens[index]['number']
                del(tokens[index-1:index + 1])
                
                index -= 3
            
        index += 1
    #print tokens
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


def test(line, expectedAnswer):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print "PASS! (%s = %f)" % (line, expectedAnswer)
    else:
        print "FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer)


# Add more tests to this function :)
def runTest():
    print "==== Test started! ===="
    test("1+2", 3)
    test("1.0+2.1-3", 0.1)
    print "==== Test finished! ====\n"

runTest()

while True:
    print '> ',
    line = raw_input()
    line.replace(' ','')
    tokens = tokenize(line)
    #print tokens
    answer = evaluate(tokens)
    print "answer = %f\n" % answer