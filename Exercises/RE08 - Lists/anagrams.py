# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:00:11 2018

@author: diogo
"""
def anagrams(alist):
    letters_list = []
    resultado = []
    resposta = []
    lista = []
    prev_anagram = []
    anagram = []
    for words in alist:
        words = words.lower()
        words = sorted(words.replace(" ", ""))
        words = "".join(words)
        letters_list += [words,]
    for idx1, sequence in enumerate(letters_list):
        occur = letters_list.count(sequence)
        count = 0
#        while count != occur:
        for idx2, i in enumerate(letters_list):
            if i == sequence:
                resultado += [idx2]
                count += 1
        resposta += [resultado]       
        resultado = []
        
    for i in resposta:
        if i not in lista:
            lista.append(i)
    
    for i in lista:
        for j in i:
            prev_anagram += [alist[j]]
        prev_anagram = sorted(prev_anagram)
        anagram += [prev_anagram]
        prev_anagram = []
                  
    return sorted(anagram, key=lambda x: x[0].lower())