#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  
"""
Date: 2019/11/28
Author: Xiao-Le Deng
Email: xiaoledeng at gmail.com
Function: write a list into the file
"""

def write_list_to_file(l,file):
    """write a list into the file, 'l' is the list and 'file' is the saved file"""
    with open(file,'w') as f:
        for i,j in enumerate(l):
            x = str(j)+'\n'
            f.write(x)

# example
# l =[1,2,3,4,5]
# l =['a','d',1,2,4]
# write_list_to_file(l,"writefile.txt")