#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  
"""
Date: 2019/11/27
Author: Xiao-Le Deng
Email: xiaoledeng at gmail.com
Function: get the intersection between two lists
"""

def list_intersection(list_a,list_b):
    '''get the intersection between two lists'''
    return list(set(list_a).intersection(set(list_b)))

a = [1,2,3]
b = [2,3,4]

c = list_intersection(a, b)
d = list_intersection(b, a)

print(c)
print(d)