# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 01:47:20 2018

@author: diogo
"""

def flatten(alist):
    for idx, element in enumerate(alist):
        if type(element) is list:
            alist.remove(element)
            for item in element:
                alist.insert(idx, item)
                idx += 1
            return flatten(alist)   
    return alist