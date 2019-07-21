#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 12:24:34 2018

@author: up201806250
"""

def translate(astring, table):
    result = ""
    subs = ""
    for letter in astring:
        for i in table:
            if letter in i:
                subs = str(i[1])
                print(subs)
                break
            else:
                subs = letter
        print(i)
        result += subs
    return result
                
    

        
a = "Hello world! "
t = (('a', 1), ('e', 2), ('i', 3), ('o', 4), ('u', 5), ('!', ' :)'))
print(translate(a, t))


