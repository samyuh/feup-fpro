#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:36:53 2018

@author: up201806250
"""

def formal(name):
    name_list = name.split()
    count = len(name_list)-1
    form = name_list[count] + ", "
    for i in name_list: 
        if i != name_list[count]:
            form += i[0] + ". "
    return form

print(formal("Diogo Samuel Fernandes"))