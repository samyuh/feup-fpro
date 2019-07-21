#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 12:20:53 2018

@author: up201806250
"""

def count(word, phrase):
    numero_palavras = 0
    word = word.lower()
    phrase = phrase.lower()
    frase_lista = phrase.split()
    for i in frase_lista:
        if word == i:
            numero_palavras += 1
    return numero_palavras