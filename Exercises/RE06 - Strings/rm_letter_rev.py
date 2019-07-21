#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:43:09 2018

@author: up201806250
"""

def rm_letter_rev(l, astr): 
        contador = 0
        frase = ""
        while contador < len(astr):
            if astr[contador] != l:
                frase = astr[contador] + frase
            contador += 1
        return frase 