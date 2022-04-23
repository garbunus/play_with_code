#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 00:26:14 2021

@author: eduardogarbin
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score, cluster
from scipy.spatial.distance import cdist
from sklearn.metrics.pairwise import euclidean_distances as srEuclides
import plotly.figure_factory as ff
from plotnine import *


plt.figure(figsize=(12, 12))


#CLUSTER HIERARQUICO
#leitura de dados e criação de dataframa
pokemon = pd.read_csv('pokemon.csv')
#reset index para nomes
pokemon.set_index('Name', inplace=True) 
#padronização de escalas

#Calcular distancia Euclidiana para as variáveis
pokemon_euclid = srEuclides(pokemon[['Attack', 'Defence']], pokemon[['Attack','Defence']])
##Calculo de clusters hierarquicos
pokemon_aglomerative = pd.DataFrame(AgglomerativeClustering(linkage='ward', n_clusters=10).fit(pokemon[['HP', 'Sp_attack']]).labels_)
kkmeans = KMeans(n_clusters=3)
pokemon_aglomerative2 = pd.DataFrame(kkmeans.fit(pokemon[['HP', 'Sp_attack']]).labels_)
pokemon_aglomerative3 = pd.DataFrame(DBSCAN().fit(pokemon[['HP', 'Sp_attack']]).labels_)

pokemonFull = pd.concat([pokemon, pokemon_aglomerative], axis=1, join='inner')
pokemonFull2 = pd.concat([pokemon, pokemon_aglomerative2], axis=1, join='inner')
pokemonFull3 = pd.concat([pokemon, pokemon_aglomerative3], axis=1, join='inner')

#rename columns
pokemonFull = pokemonFull.rename(columns={0: 'grupo'})
pokemonFull2 = pokemonFull2.rename(columns={0: 'grupo'})
pokemonFull3 = pokemonFull3.rename(columns={0: 'grupo'})
pokemonFull
#%%

#construção dos gráficos
def plotSingle(): 
    plt.scatter(pokemonFull['HP'], pokemonFull['Sp_attack'], c=pokemonFull[0])
    plt.subplot(221)
    plt.title('Ward')
    
def plotKmeans():
    plt.scatter(pokemonFull2['HP'], pokemonFull2['Sp_attack'], c=pokemonFull2[0])
    plt.subplot(222)
    plt.title('Kmeans')
    
def plotDBScan():
    plt.scatter(pokemonFull3['HP'], pokemonFull3['Sp_attack'], c=pokemonFull3[0])
    plt.subplot(223)
    plt.title('DBSCAN')
 #%%
   
#plotagem dos gráficos
plotSingle()
plotKmeans()
plotDBScan()
plt.show()

sns.scatter(pokemonFull['HP'], pokemonFull['Sp_attack'], c=pokemonFull[0])

#olhando alguns dados
mediaPura = pokemon.mean()
mediaCluster = pokemonFull.groupby(0).mean()





