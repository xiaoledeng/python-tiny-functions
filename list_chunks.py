#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  
"""
Date: 2019/11/27
Author: Xiao-Le Deng
Email: xiaoledeng at gmail.com
Function: split a list into evenly sized chunks
from https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
"""

def list_chunks(list, n):
    """split a list into evenly sized chunks"""
    for i in range(0, len(list), n):
        yield list[i:i + n]

# a = [1,2,3,4,5,6,7,8,9]
# b = list(list_chunks(a, 3))
# b0 = b[0]
# b1 = b[1]

# print(b)
# print(b0,b1)
