# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 18:05:36 2018

@author: diogo
"""
def wc(filename):
    count_line = 0
    count_words = 0
    count_char = 0
    with open(filename, "r") as file:
        for line in file:
            count_line += 1
            words = line.split()
            count_words += len(words)
            for char in line:
                count_char += 1
    return (count_line, count_words, count_char)