#!/usr/local/bin/python3
# -*- coding: utf-8 -*-  
"""
Date: 2019/11/27
Author: Xiao-Le Deng
Email: xiaoledeng at gmail.com
Function: remove duplicates in a given list
"""

def list_remove_duplicate(original_list):
    format_list = list(set(original_list))
    format_list.sort(key=original_list.index)
    return format_list

List1 = [1,1,1]
List2 = ["John","John","John","Mark","David","David","Shalom","Shalom","Shalom"]

print(list_remove_duplicate(List1))
print(list_remove_duplicate(List2))