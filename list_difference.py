#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  
"""
Date: 2019/11/27
Author: Xiao-Le Deng
Email: xiaoledeng at gmail.com
Function: get the difference of first list between two lists
"""

def list_difference(list_a,list_b):
    '''get the difference of first list between two lists'''
    return list(set(list_a).difference(set(list_b)))

# a = [1,2,3]
# b = [2,3,4]

# c = list_difference(a,b)
# d = list_difference(b,a)

# print(c)
# print(d)