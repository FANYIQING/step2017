# -*- coding: utf-8 -*-
"""
Created on Sat May 27 15:57:46 2017

@author: Administrator
"""
def a_in_b (a, b):
    cp_b = list(b)    #deep copy
    for i in a:
        if i in cp_b:
            cp_b.remove(i)
        else:
            return False
    return True

def qu(l):
    ret = l
    tmp = list()
    e = enumerate(ret)    
    for i, c in e:
        if c == 'q':
            tmp.append(i)
            
    
    for i, n in enumerate(tmp):
        b = ret[n-i+2:]
        ret = ret[:n-i]
        ret.append('qu')
        ret.extend(b)
        
        
    return ret

def ini():
    file_object = open('dict.txt','r')
    dic = dict()
    for line in file_object.readlines():
        line = line.lower()
        line = list(line.strip('\n'))
        score = 0
        line = qu(line)
        for i in line:
            
            if i in ['qu', 'j', 'k', 'x', 'z']:
                score += 3
            
            elif i in [ 'c', 'f', 'h', 'l', 'm', 'p', 'v', 'w', 'y']:  
                score += 2
            else:
                score +=1
        dic[tuple(line)] = (score+1)**2
    file_object.close()
    #type of return is a list 
    return sorted(dic.iteritems(), key = lambda x: x[1], reverse = True) 

def run(letters, dic_in_order):
    
    
    
    letters = qu(letters)
    
#    print letters
    for i in dic_in_order:
        if a_in_b(i[0], letters):
            return "".join(i[0]), i[1]
    return 0, 0
        

if __name__ == '__main__':
    dic_in_order=ini()
    print dic_in_order
    
    
