#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 17:36:39 2021

@author: eduardogarbin
"""

import numpy as np

def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

def sigmoidDerivada(sig):
    return sig * (1 - sig)

def calculaDeltaSaida(erro, derivada):
    return erro * derivada

def calculaDeltaOculta(deltaSaida, pesos, derivada):
    pesoTransposta = pesos.T
    pesoXdeltaSaida = deltaSaida.dot(pesoTransposta)
    return pesoXdeltaSaida * derivada

def correcaoDePesos(erros, camadas):
    pass

def novo_peso(deltaXentrada, momento, pesoOriginal, learningRate):
    return (pesoOriginal * momento) + (deltaXentrada * learningRate)
    
a = sigmoidFunction(0.5)
b = sigmoidDerivada(a)


entradas = np.array([[0,0],
                     [0,1],
                     [1,0],
                     [1,1]])

saidas = np.array([[0], [1], [1], [0]])

#pesos_zero = np.array([[-0.424, -0.740, -0.961], 
 #                     [0.358, -0.577, -0.469]])

#pesos_um = np.array([[-0.017], [-0.893], [0.148]])

pesos_zero = 2*np.random.random((2,3)) -1
pesos_um = 2*np.random.random((3,1)) -1


#training time
epocas = 10 #quantidade de vezez que vou reavaliar os pesos 
 #momento
momento = 1
#learning rate
learning_rate = 0.3


for j in range(epocas):
    camadaEntrada = entradas
    #camada oculta
    somaSinapseZero = np.dot(camadaEntrada, pesos_zero)
    camadaOculta = sigmoidFunction(somaSinapseZero)
    #camada final
    somaSinapseUm = np.dot(camadaOculta, pesos_um)
    camadaSaida = sigmoidFunction(somaSinapseUm)
    #calculo de erros
    erros = saidas - camadaSaida
    #avaliação de desempenho
    mediaAbsoluta = np.mean(np.abs(erros))
    print(1 - mediaAbsoluta)
    
    
    
 
    #calculando desta da camada de saída
    deltaSaida = calculaDeltaSaida(erros, sigmoidDerivada(camadaSaida))
    #calculando o delta da camada oculta
    deltaOculta = calculaDeltaOculta(deltaSaida, pesos_um, sigmoidDerivada(camadaOculta))
    #transpondo a matrix de resultados da camada oculta
    ocultran = camadaOculta.T
    # desta multiplicado pela entrada
    deltaXentrada = np.dot(ocultran, deltaSaida)    
    #calculando novos pesos
    pesos_um = novo_peso(deltaXentrada, momento, pesos_um, learning_rate)
    #calculando delta da camada de entrada
    deltaEntrada = calculaDeltaOculta(deltaOculta, pesos_zero, sigmoidDerivada(camadaEntrada))
    print(deltaEntrada)
    #multiplicação da entrada com o delta da camada oculta
    deltaPelaEntrada = np.dot(camadaEntrada, deltaEntrada.T)
    print(deltaPelaEntrada)
    #pessos da primeira sinapse
    pesos_zero = novo_peso(deltaPelaEntrada, momento, pesos_zero, learning_rate)
    
    
    
    mediaAbsoluta = np.mean(np.abs(erros))
    acerto = 1 - mediaAbsoluta 