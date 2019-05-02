import numpy as np
import random
import collections
import copy
import matplotlib.pyplot
import sys
from caixeiroviajante.funcaoAptidao import apt_func

# Matriz da populacao com 20 membros.
populacao = np.zeros((20, 20), dtype=np.float)

# Variaveis.
n_cidades = 20
n_geracoes = 10000
taxa_mutacao = 0.05

# Define populacao aleatória.
for i in range(n_cidades):
    populacao[i] = random.sample(range(n_cidades), n_cidades)

# ?
x = np.random.rand(1, n_cidades)
y = np.random.rand(1, n_cidades)

# Chama a funcao apt_funcao, responsavel por calcular a aptidão do caixeiro viajante em sua jornada.
lista_aptidao = apt_func(populacao[:, :], x, y, n_cidades)

# Cria o array que irá armazenar a população ordenada por resultado da função de aptidão.
populacao_ordenada = np.zeros((20, 20), dtype=np.float)

# Ordena a população de acordo com o resultado da execução da função de aptidão.
for i in range(n_cidades):
    populacao_ordenada[i, :] = populacao[int(lista_aptidao[i, 0]), :]

# Inicia o array que irá armazenar as possibilidades da roleta, onde o melhor colocado na ordenação pelo resultado da
# execução da função de aptidão terá mais chances de ser "sorteado".
roleta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          1, 1, 1, 1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2, 2, 2,
          3, 3, 3, 3, 3, 3, 3,
          4, 4, 4, 4, 4, 4,
          5, 5, 5, 5, 5,
          6, 6, 6, 6,
          7, 7, 7,
          8, 8,
          9]

# Array que será utilizado como referência para montagem do gráfico no final da execução do algoritmo.
array_plot = []

# Indice da geração para controle do laço de repetição.
indice_geracao = 0

while indice_geracao < n_geracoes:
    # Sorteia os números que serão utilizados na roleta.
    grupo_pais1 = random.sample(range(0, 55), 5)
    grupo_pais2 = random.sample(range(0, 55), 5)

    posicao_filho1 = 10
    posicao_filho2 = 11

    ii = 0
    while ii < 5:
        # print grupo_pais1[i]
        # print roleta[grupo_pais1[i]]
        # print populacao_ordenada[roleta[grupo_pais1[i]], :]
        filho1 = copy.deepcopy(populacao_ordenada[roleta[grupo_pais1[ii]], :])
        filho2 = copy.deepcopy(populacao_ordenada[roleta[grupo_pais2[ii]], :])

        posicao_corte = random.randint(0, 19)

        corte1 = filho1[posicao_corte]
        corte2 = filho2[posicao_corte]

        filho1[posicao_corte] = corte2
        filho2[posicao_corte] = corte1

        indice_repetido_ant = copy.deepcopy(posicao_corte)

        while True:
            cidade_repetida = [item for item, count in collections.Counter(filho1).items() if count > 1]
            if cidade_repetida:
                # print "valor repetido " + str(cidade_repetida)
                for indice_repetido, e in list(enumerate(filho1)):
                    if e == cidade_repetida and indice_repetido != indice_repetido_ant:
                        corte_repetido1 = filho1[indice_repetido]
                        corte_repetido2 = filho2[indice_repetido]

                        filho1[indice_repetido] = corte_repetido2
                        filho2[indice_repetido] = corte_repetido1

                        indice_repetido_ant = copy.deepcopy(indice_repetido)
                        break
            else:
                break

        populacao_ordenada[posicao_filho1, :] = copy.deepcopy(filho1)
        populacao_ordenada[posicao_filho2, :] = copy.deepcopy(filho2)
        posicao_filho1 += 2
        posicao_filho2 += 2
        ii += 1

    # Mutação de genes.
    i_mutacao = random.randint(0, 19)
    pos_mutacao = random.sample(range(0, 19), 2)

    mut_a = copy.deepcopy(populacao_ordenada[i_mutacao, pos_mutacao[0]])
    mut_b = copy.deepcopy(populacao_ordenada[i_mutacao, pos_mutacao[1]])

    populacao_ordenada[i_mutacao, pos_mutacao[0]] = mut_b
    populacao_ordenada[i_mutacao, pos_mutacao[1]] = mut_a

    lista_aptidao = apt_func(populacao_ordenada[:, :], x, y, n_cidades)
    array_plot.append(lista_aptidao[0, 1])

    populacao_ordenada_aux = copy.deepcopy(populacao_ordenada)
    for i in range(n_cidades):
        populacao_ordenada[i, :] = populacao_ordenada_aux[int(lista_aptidao[i, 0]), :]

    indice_geracao += 1

# Imprime resultados finais na janela de comando e exibe o gráfico.
print("Tamanho da Populacao: " + str(np.size(populacao_ordenada, 0)))
print("Taxa de Mutacao: " + str(taxa_mutacao))
print("Numero de Cidades: " + str(n_cidades))
print("Melhor Custo: " + str(lista_aptidao[0, 1]))
print("Melhor Solucao: " + str(populacao_ordenada[0, :]))
matplotlib.pyplot.ylim(3, 10)
matplotlib.pyplot.plot(array_plot)
matplotlib.pyplot.show()

# Finaliza a execução do algoritmo
sys.exit()