#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy


def apt_func(populacao, distanciacidades, n_rotas):
    # Gera a matriz 20x21 da população onde a última coluna é a cópia da primeira coluna.
    # A última coluna é igual a primeira pois o caixeiro viajante precisa retornar a cidade original.
    tour = numpy.c_[populacao, populacao[:, 0]]

    # Cria uma matrix 20x2 para receber a aptidão de cada cromossomo.
    # A primeira coluna corresponde ao índice do cromossomo na matriz de população.
    # A segunda coluna representa o valor de aptidão
    v_aptidao = numpy.zeros((20, 2), dtype=numpy.float)

    # Percorre o total de rotas existentes no algoritmo. Neste exemplo, cada rota representa um membro da população.
    for i in range(0, n_rotas):
        v_aptidao[i, 0] = i
        v_aptidao[i, 1] = 0
        # Para cada cidade calcula a v_aptidaoância entre ela e a próxima cidade.
        for j in range(0, n_rotas):
            v_aptidao[i, 1] += distanciacidades[int(tour[i, j]), int(tour[i, j + 1])]

    # Loop para converter os índices do vetor de aptidão em inteiros.
    for i in range(0, n_rotas):
        v_aptidao[i, 0] = int(v_aptidao[i, 0])

    # Utiliza a função sorted para ordenar a matriz pela segunda coluna, correspondente ao valor de aptidão.
    v_aptidao = sorted(v_aptidao, key=lambda x: x[1])
    v_aptidao = numpy.array(v_aptidao)

    return v_aptidao
