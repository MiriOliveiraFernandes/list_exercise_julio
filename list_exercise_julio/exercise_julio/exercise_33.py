# 33. Ler uma matriz A de 4 x 4, calcular e escrever as somas dos elementos marcados com o
# X. Utilizar estruturas de repetição.

import numpy as np

a  = np.array([
    [ 35,  72,  64,  18 ],
    [ 90,  27,  56,  81 ],
    [ 43,  88,  12,  50 ],
    [ 68,  19,  77,  93 ]])

def soma_4_primeiros(matriz):
    soma = 0
    for l in range(matriz.shape[0]): 
            if l <= 1: 
                for c in range(matriz.shape[1]):  
                    if c <= 1: 
                        soma += matriz[l][c]             
    print(f'Esse é o valor da soma dos elementos marcados com "X": {soma}')

def soma_4_ultimos(matriz):
    soma = 0
    for l in range(matriz.shape[0]): 
            if l >= 2: 
                for c in range(matriz.shape[1]):  
                    if c >= 2: 
                        soma += matriz[l][c]             
    print(f'Esse é o valor da soma dos elementos marcados com "X": {soma}')

def soma_piramide(matriz):
    soma = 0 
    for l in range(matriz.shape[0]): 
        if l <= 3:  
            for c in range(matriz.shape[1]):  
                if c <= l:  
                    soma += matriz[l][c]  
    print(f'Esse é o valor da soma dos elementos marcados com "X": {soma}')

def soma_piramide_invertida(matriz):
    soma = 0 
    for l in range(matriz.shape[0]):
        if l == 0:  
            for c in range(1, 4):  
                soma += matriz[l][c]
                print(f'Somando elemento: {matriz[l][c]} (linha {l}, coluna {c})')
        elif l == 1: 
            for c in range(2, 4):  
                soma += matriz[l][c]
                print(f'Somando elemento: {matriz[l][c]} (linha {l}, coluna {c})')
        elif l == 2: 
            soma += matriz[l][3]  
            print(f'Somando elemento: {matriz[l][3]} (linha {l}, coluna 3)')
        

                  
    print(f'Esse é o valor da soma dos elementos marcados com "X": {soma}')                 
# soma_4_primeiros(a)
# soma_piramide(a)
# soma_4_ultimos(a)
soma_piramide_invertida(a)