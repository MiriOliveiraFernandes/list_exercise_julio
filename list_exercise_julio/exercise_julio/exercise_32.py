# 32. Ler 2 matrizes, A 4 x 6 e B 4 x 6 e criar:
# a) uma matriz S que seja a soma de A e B.
# b) uma matriz D que seja a diferença de A e B. (A – B).
# Escrever as matrizes S e D após todo cálculo estar concluído.

import numpy as np

# Definindo as matrizes A e B
A = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16],
              [17,18,19,20],
              [21,22,23,24]
              ])

B = np.array([[35, 38, 33, 41],
              [39, 45, 41, 46],
              [52, 60, 57, 55],
              [47, 50, 54, 58],
              [63, 64, 70, 69],
              [71, 75, 80, 78]])

# Realizando a soma e a subtração
s = A + B
d = A - B

# Imprimindo os resultados
print(f'A soma das matrizes é:\n{s}')
print(f'A subtração das matrizes é:\n{d}')
