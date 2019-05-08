#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import random
import collections
import copy
import matplotlib.pyplot
import sys
import time
import math
# from caixeiroviajante.funcaoAptidao import apt_func
from funcaoAptidao import apt_func

# Esse algoritmo tem como objetivo realizar a implementação de um algoritmo genético baseado no caixeiro viajante

# Salva o instante de início da execução do algoritmo
start = time.time()

# Cria a matriz da populacção com 20 membros
populacao = numpy.zeros((20, 20), dtype=numpy.float)

# Número total de indivíduos na população
n_individuos = 20
# Total de gerações que o algoritmo irá executar
n_geracoes = 10000
# Essa variação está aqui para representar a possibilidade de cada membro ser escolhido para mutação
taxa_mutacao = 0.05

# Habita a população com membros aleatórios
for i in range(n_individuos):
    populacao[i] = random.sample(range(n_individuos), n_individuos)

# As variáveis x e y representam os vetores com a posição de cada cidade
x = numpy.random.rand(1, n_individuos)
y = numpy.random.rand(1, n_individuos)

# Cria matriz que irá representar a distância entre as cidades
distancia_cidade = numpy.zeros((20, 20), dtype=numpy.float)

# Calcula a distância entre cada cidade
for i in range(0, n_individuos):
    for j in range(0, n_individuos):
        distancia_cidade[i, j] = math.sqrt(math.pow(x[0, i] - x[0, j], 2) + math.pow(y[0, i] - y[0, j], 2))

# Utiliza a função apt_funcao, responsável por calcular a aptidão de cada indivíduo
lista_aptidao = apt_func(populacao[:, :], distancia_cidade[:, :], n_individuos)

# Cria o array que irá armazenar a população ordenada por resultado da função de aptidão
populacao_ordenada = numpy.zeros((20, 20), dtype=numpy.float)

# Ordena a população de acordo com o resultado da execução da função de aptidão
for i in range(n_individuos):
    populacao_ordenada[i, :] = populacao[int(lista_aptidao[i, 0]), :]

# Inicia o array que irá armazenar as possibilidades da roleta, onde o melhor colocado na matriz de aptidão terá mais
# chances de ser escolhido.
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

# Array que será utilizado como referência para montagem do gráfico no final da execução do algoritmo
array_plot = []

# Índice da geração para controle do laço de repetição
indice_geracao = 0

while indice_geracao < n_geracoes:
    # Sorteia os números que serão utilizados na roleta
    # São escolhidos dois grupos de pais com 5 indivíduos em cada
    grupo_pais1 = random.sample(range(0, 55), 5)
    grupo_pais2 = random.sample(range(0, 55), 5)

    # Essas variáveis serão utilizadas para indicar a posição dos filhos na matriz da população
    posicao_filho1 = 10
    posicao_filho2 = 11
    
    # Variável utilizada no controle de crossover entre os pais
    i_pais = 0
    while i_pais < 5:
        # Realiza uma cópia do filho com base no índice retirado da roleta
        filho1 = copy.deepcopy(populacao_ordenada[roleta[grupo_pais1[i_pais]], :])
        filho2 = copy.deepcopy(populacao_ordenada[roleta[grupo_pais2[i_pais]], :])

        # Define uma posição aleatória de corte para ser utilizado na técnica de cycle
        posicao_corte = random.randint(0, 19)

        # Busca o gene (cidade) que será trocado em cada filho
        corte1 = filho1[posicao_corte]
        corte2 = filho2[posicao_corte]

        # Realiza a troca das cidades selecionadas
        filho1[posicao_corte] = corte2
        filho2[posicao_corte] = corte1

        # Índice criado para evitar que op rogram
        indice_repetido_ant = copy.deepcopy(posicao_corte)

        # Após feita a primeira troca com o método cycle existe a possibilidade de um cidade (gene) estar repetida em um
        # indivíduo (cromossomo). Essa repetição serve para continuar trocando as cidades repetidas do primeiro filho,
        # até que não existe mais nenhum repetido
        while True:
            # Identifica se existe cidade repetida no primeiro filho
            cidade_repetida = [item for item, count in collections.Counter(filho1).items() if count > 1]
            if cidade_repetida:
                for indice_repetido, e in list(enumerate(filho1)):
                    # Encontra o índice da cidade repetida do filho1 e troca com o filho2
                    if e == cidade_repetida and indice_repetido != indice_repetido_ant:
                        corte_repetido1 = filho1[indice_repetido]
                        corte_repetido2 = filho2[indice_repetido]

                        filho1[indice_repetido] = corte_repetido2
                        filho2[indice_repetido] = corte_repetido1

                        # Copia o índice em que foi realizada a troca para evitar loop, trocando sempre a mesma posição
                        indice_repetido_ant = copy.deepcopy(indice_repetido)
                        break
            else:
                break

        # Insere os filhos na população
        populacao_ordenada[posicao_filho1, :] = copy.deepcopy(filho1)
        populacao_ordenada[posicao_filho2, :] = copy.deepcopy(filho2)
        posicao_filho1 += 2
        posicao_filho2 += 2
        i_pais += 1

    # Mutação da população
    # Seleciona aleatoriamente um indivíduo para sofrer mutação
    i_mutacao = random.randint(0, 19)
    # Seleciona as duas cidades que terão sua posição trocada
    pos_mutacao = random.sample(range(0, 19), 2)

    # Realiza a mutação
    mut_a = copy.deepcopy(populacao_ordenada[i_mutacao, pos_mutacao[0]])
    mut_b = copy.deepcopy(populacao_ordenada[i_mutacao, pos_mutacao[1]])

    populacao_ordenada[i_mutacao, pos_mutacao[0]] = mut_b
    populacao_ordenada[i_mutacao, pos_mutacao[1]] = mut_a

    # Chama novamente a função parar calcular a aptidão da população, agora com os filhos
    lista_aptidao = apt_func(populacao_ordenada[:, :], distancia_cidade[:, :], n_individuos)
    array_plot.append(lista_aptidao[0, 1])

    populacao_ordenada_aux = copy.deepcopy(populacao_ordenada)
    # Ordena a população pelo vetor de aptidão
    for i in range(n_individuos):
        populacao_ordenada[i, :] = populacao_ordenada_aux[int(lista_aptidao[i, 0]), :]

    indice_geracao += 1

# Salva o instante de "término" da execução do algoritmo.
end = time.time()

# "Calcula" o tempo (em segundos") de execução do algoritmo.
executionTime = str("%.1f" % (end - start))

# Imprime resultados finais na janela de comando e exibe o gráfico.
print("")
print("O algoritmo levou " + executionTime + " segundos para executar")
print("")
print("-------------------------------------------------------------------------------")
print("")
print("Resultados:")
print("")
print("Tamanho da Populacao: " + str(numpy.size(populacao_ordenada, 0)))
print("Taxa de Mutacao: " + str(taxa_mutacao))
print("Numero de Cidades: " + str(n_individuos))
print("Melhor Custo: " + str(lista_aptidao[0, 1]))
print("Melhor Solucao: " + str(populacao_ordenada[0, :]))
print("")

# Exibe gráfico com as melhores aptidões
matplotlib.pyplot.ylim(3, 10)
matplotlib.pyplot.plot(array_plot)
matplotlib.pyplot.show()

# Finaliza a execução do algoritmo
sys.exit()
