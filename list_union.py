#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  
"""
Date: 2019/11/27
Author: Xiao-Le Deng
Email: xiaoledeng at gmail.com
Function: get the union between two lists
"""

def list_union(list_a,list_b):
    return list(set(list_a).union(set(list_b)))

# a = [1,2,3]
# b = [2,3,4]

# print(list_union(a,b))
# print(list_union(b,a))