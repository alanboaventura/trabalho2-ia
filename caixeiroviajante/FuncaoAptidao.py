import numpy as np
import math
import copy


def apt_func(populacao, x, y, n_cidades):
    tour = np.c_[populacao, populacao[:, 0]]

    distancia_cidade = np.zeros((20, 20), dtype=np.float)

    # Distância entre as cidades
    for i in range(0, n_cidades):
        for j in range(0, n_cidades):
            distancia_cidade[i, j] = math.sqrt(math.pow(x[0, i] - x[0, j], 2) + math.pow(y[0, i] - y[0, j], 2))

    # Gera a matriz 20x21 da populacao onde a ultima coluna é a cópia da primeira coluna (o agente deve voltar a cidade)
    dist = copy.deepcopy(populacao[:, 0:2])

    # Custo de cada cromossomo - a soma das distancias para cada individuo
    for i in range(0, n_cidades):
        dist[i, 0] = i
        dist[i, 1] = 0
        # Soma das distancias para cada cromossomo
        for j in range(0, n_cidades):
            dist[i, 1] = dist[i, 1] + distancia_cidade[int(tour[i, j]), int(tour[i, j + 1])]

    for i in range(0, n_cidades):
        dist[i, 0] = int(dist[i, 0])

    dist = sorted(dist, key=lambda x: x[1])
    dist = np.array(dist)

    return dist
