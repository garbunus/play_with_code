#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 14:51:01 2021

@author: Eduardo Garbin

"""
#importando bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly as ply
import pyreadr
from sklearn.decomposition import FactorAnalysis, PCA
from sklearn.preprocessing import StandardScaler
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity, calculate_kmo
from statistics import stdev
from scipy.stats import zscore
#%%
#configurando figuras em alta resolução
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300


#%%
#carregamento de dados
estudantesR = pyreadr.read_r('notasfatorial.RData')
notas_estudantes = estudantesR['notasfatorial']
notas_estudantes = pd.DataFrame(notas_estudantes)
notas_estudantes.set_index(notas_estudantes['estudante'], inplace=True, drop=True)
notas_estudantes.drop('estudante', axis=1, inplace=True)
notas_estudantes.reset_index()
print(notas_estudantes.head())
#pair plot para olhar correlações nas variáveis
sns.pairplot(notas_estudantes)

#%%
#######TESTADO A MATRIX##### 
#fazendo a matriz de correlação
notacoor = notas_estudantes.corr(method='pearson')
k_all, k_model = calculate_kmo(notacoor)

#executando a normalização zscore (tirando as discrepâncias das escalas)
notasNormalizadas = notas_estudantes.apply(zscore)
sns.pairplot(notasNormalizadas)
#%%

pca = PCA(n_components=4)
pca.fit(notas_estudantes)

relatorio = pd.DataFrame()
relatorio['Eignvalues'] = pca.explained_variance_
relatorio['Variancia compatilhada'] = pca.explained_variance_ratio_
relatorio['Variancia acumulada'] = pca.explained_variance_ratio_.cumsum()
print(relatorio)
#%%
#imprimindo os dados 
print('COMPONENTES - eigvectors')
print(pca.components_)
#transposição dos dados
transp_vectors = pd.DataFrame(np.transpose(pca.components_))

print('TAXA DE VARIANCIA')
print(pca.explained_variance_ratio_)
print()
print('VARIANCIA - eignvalues')
print(pca.explained_variance_)
print()
print('Desvio padrão')
print(np.sqrt(pca.explained_variance_))
print()

#imprimindo no console dados obtidosda PCA
print(pca.singular_values_)
print(pca.mean_)
print(pca.n_components_)
print(pca.n_features_)
print(pca.n_samples_)

#%%
#scores fatoriais
#fig, ax = plt.subplots(figsize=(20, 20))

#scores obtidos no processo de componentes principais
scores = pd.DataFrame()
scores['score_1'] = transp_vectors[0] / np.sqrt(pca.explained_variance_[0])
scores['score_2'] = transp_vectors[1] / np.sqrt(pca.explained_variance_[1])
scores['score_3'] = transp_vectors[2] / np.sqrt(pca.explained_variance_[2])
scores['score_4'] = transp_vectors[3] / np.sqrt(pca.explained_variance_[3])
print(scores)

        


