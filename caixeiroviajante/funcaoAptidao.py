#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import copy

def apt_func(populacao, distancia_cidade, n_cidades):
    # Gera a matriz 20x21 da populacao onde a ultima coluna é a cópia da primeira coluna (O final é na cidade inicial).
    tour = numpy.c_[populacao, populacao[:, 0]]

    # ?
    dist = copy.deepcopy(populacao[:, 0:2])

    # Custo de cada cromossomo - a soma das distancias para cada individuo.
    for i in range(0, n_cidades):
        dist[i, 0] = i
        dist[i, 1] = 0
        # Soma das distancias para cada cromossomo.
        for j in range(0, n_cidades):
            dist[i, 1] = dist[i, 1] + distancia_cidade[int(tour[i, j]), int(tour[i, j + 1])]

    for i in range(0, n_cidades):
        dist[i, 0] = int(dist[i, 0])

    dist = sorted(dist, key=lambda x: x[1])
    dist = numpy.array(dist)

    return dist
