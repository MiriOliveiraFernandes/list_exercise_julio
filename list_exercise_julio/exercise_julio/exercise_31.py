# 31. Ler uma matriz M 5 x 5, calcular e escrever as seguintes somas:
# a) da linha 3 de M
# b) da coluna 2 de M
# c) da diagonal principal
# d) da diagonal secundária
# e) de todos os elementos da matriz
# Obs: Na figura abaixo o X indica os elementos que devem ser somados

import numpy as np

m = np.array([
            [ 72,  54,  36,  91,  18 ],
            [  4,  67,  83,  59,  39 ],
            [ 88,  26,  55,  93,  71 ],
            [ 11,  47,  65,  62,  20 ],
            [ 79,  33,  28,  90,  58 ]])
def somaLinha_3(matriz):
    somaLinha_3=0
    for l in range(matriz.shape[0]):
        if l == 3:
            for c in range(matriz.shape[1]):
                somaLinha_3 = somaLinha_3 + matriz[l][c]
    print(f'Essa é a soma da linha 3: {somaLinha_3}')

def somaColuna_2(matriz):
    somaColuna_2=0
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            if c==2:
                somaColuna_2 = somaColuna_2 + matriz[l][c]
    print(f'Essa é a soma da coluna 2: {somaColuna_2}')

def somaDiagonalP(matriz):
    somaDiagonalP=0
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            if l==c:
                somaDiagonalP = somaDiagonalP + matriz[l][c]
    print(f'Essa é a soma da diagonal principal: {somaDiagonalP}')

def somaDiagonalS(matriz):
    somaDiagonalS=0
    cont=4
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
            if c==cont:
                somaDiagonalS = somaDiagonalS + matriz[l][c]
                cont = cont - 1

    print(f'esse é a soma da diagonal secundaria: {somaDiagonalS}')

def somaMatriz(matriz):
    soma = 0
    for l in range(matriz.shape[0]):
        for c in range(matriz.shape[1]):
           
             soma = soma + matriz[l][c]
    # return soma

    print(f'Esse é o valor da soma da matriz: {soma}')

# print(sum(m))
somaLinha_3(m)
somaColuna_2(m)
somaDiagonalP(m)
somaDiagonalS(m)
somaMatriz(m)