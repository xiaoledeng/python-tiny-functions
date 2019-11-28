#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  
"""
Date: 2019/11/27
Author: Xiao-Le Deng
Email: xiaoledeng at gmail.com
Function: get a list of each line in the file
"""

def read_file_to_list(file):
    """Return a list of each line in the file"""
    result=[]
    with open(file,'rt',encoding='utf-8') as f:
        for line in f:
            result.append(list(line.strip('\n').split(','))[0])
    return result

# # example
# a = read_file_to_list("example.txt")
# print('The len of the list is:',len(a))
# print(a)