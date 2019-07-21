#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:47:58 2018

@author: up201806250
"""

def unique(atuple):
    sort = tuple(sorted(atuple))
    result = ()
    for (i, number) in enumerate(sort):
        if number not in result:
            result = result + (number, )
    return result