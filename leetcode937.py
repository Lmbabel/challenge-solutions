# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:13:24 2020

@author: Lucas
"""

logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]
def sortByMid(elem):
    return elem.partition(" ")[2]

letter_list = []
ID_list = []

idx = 0
maxl = len(logs)
while idx < len(logs):
    if sortByMid(logs[idx])[0].isalpha():
        letter_list.append(logs[idx])
        logs.remove(logs[idx])
    else:    
        idx+=1
            
letter_list.sort(key=sortByMid)
print(letter_list + logs)
        
        


#print(sortedAlphas + logs)
    