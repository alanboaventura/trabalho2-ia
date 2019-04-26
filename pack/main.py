import numpy as np
import random
from pack.funcaoAptidao import apt_func
# matriz da populacao com 20 membros
populacao = np.zeros((20, 20), dtype=np.float)

# variaveis
nCidades = 20
nGeracoes = 10000

# define populacao aleatoria
for i in range(nCidades):
    populacao[i] = random.sample(range(nCidades), nCidades)

# for i in range(nCidades):
#    print populacao[i]

x = np.random.rand(1, nCidades)
y = np.random.rand(1, nCidades)

lista_aptidao = apt_func(populacao[:, :], x, y, nCidades)
print lista_aptidao

populacao_ordenada = np.zeros((20, 20), dtype=np.float)

for i in range(nCidades):
    populacao_ordenada[i, :] = populacao[int(lista_aptidao[i,0]), :]

print populacao_ordenada

# funcao de apitadao
