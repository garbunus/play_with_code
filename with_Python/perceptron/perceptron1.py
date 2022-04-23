#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 21:30:47 2021

@author: eduardogarbin
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Perceptron incial

entradas = [1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        s += e[i] * p[i]
        
    return s
        
        
        
s = soma(entradas, pesos)
print(s)


def stepFunction(soma):
    if (soma >= 1):
        return 1
    else:
        return 0
    
r = stepFunction(s)
print(r)