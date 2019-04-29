import numpy as np
import random
from caixeiroviajante.FuncaoAptidao import apt_func

# Variaveis
nCidades = 20
nGeracoes = 10000

# Matriz da populacao
populacao = np.zeros((nCidades, nCidades), dtype=np.float)

# Define populacao aleatoria
for i in range(nCidades):
    populacao[i] = random.sample(range(nCidades), nCidades)

x = np.random.rand(1, nCidades)
y = np.random.rand(1, nCidades)

lista_aptidao = apt_func(populacao[:, :], x, y, nCidades)
print(lista_aptidao)

populacao_ordenada = np.zeros((20, 20), dtype=np.float)

for i in range(nCidades):
    populacao_ordenada[i, :] = populacao[int(lista_aptidao[i, 0]), :]

print(populacao_ordenada)


