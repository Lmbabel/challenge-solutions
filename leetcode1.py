# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 23:21:01 2020

@author: Lucas
"""


List = [3, 3]
target = 6

table = {}
for idx, val in enumerate(List):
    if val < target:
        table[val] = idx
for key in table:
    compl = target - key
    if compl in table and table.get(compl) != table.get(key):
        print([table.get(key), table.get(compl)])
        break