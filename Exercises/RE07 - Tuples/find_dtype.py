#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:13:21 2018

@author: up201806250
"""

def find_dtype(atuple, data_type):
    result = ()
    for (i, value) in enumerate(atuple):
        value_type = type(value).__name__
        if value_type == data_type:
            result = result + (value, )
    return result
        
        
a = (1, 2, 3)
d = "float"

print(find_dtype(a, d))