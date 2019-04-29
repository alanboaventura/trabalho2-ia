import numpy as np
import random
from pack.funcaoAptidao import apt_func

# matriz da populacao com 20 membros
populacao = np.zeros((20, 20), dtype=np.float)

# variaveis
n_cidades = 20
n_geracoes = 10000

# define populacao aleatoria
for i in range(n_cidades):
    populacao[i] = random.sample(range(n_cidades), n_cidades)

x = np.random.rand(1, n_cidades)
y = np.random.rand(1, n_cidades)

# chama a funcao apt_funcao, responsavel por calcular a
lista_aptidao = apt_func(populacao[:, :], x, y, n_cidades)

# print(lista_aptidao)

populacao_ordenada = np.zeros((20, 20), dtype=np.float)

for i in range(n_cidades):
    populacao_ordenada[i, :] = populacao[int(lista_aptidao[i,0]), :]

# print(populacao_ordenada)

taxa_mutacao = 0.05

# imprime resultados finais na janela de comando
print("Tamanho da População: " + str(np.size(populacao_ordenada, 0)))
print("Taxa de Mutacao: " + str(taxa_mutacao))
print("Número de Cidades: " + str(n_cidades))
print("Melhor Custo: " + str(lista_aptidao[0, 1]))
print("Melhor Solução: " + str(populacao_ordenada[0, :]))