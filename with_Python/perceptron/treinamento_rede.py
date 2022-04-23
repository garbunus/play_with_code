#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 13:11:46 2021

@author: eduardogarbin
"""

import numpy as np
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0,0,0,1])
#entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
#saidas = np.array([0,1,1,1]) 
entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0,1,1,0])         
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.5

def stepFunction(soma):
    if (soma >= 1):
        return 1
    else:
        return 0           
    
def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado para:' + str(pesos[j]))
            print('Total de erros:' + str(erroTotal))
            
treinar()