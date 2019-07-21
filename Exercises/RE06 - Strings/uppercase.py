#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:53:17 2018

@author: up201806250
"""

def uppercase(astring):
    frase = astring
    for i in range(3):
        if astring[i] != astring[i].lower():
            frase = astring.upper()
    return frase