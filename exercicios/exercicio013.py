#        0 1 2 3(lista) 4(tupla)   5(lista) 6(lista)
lista = [0,1,2,3, ('ooi', 55), [5,6,7,8], ['opa', 90]]
#posicao 3 -> n-1 -> 4-1 = 3
print(lista[-1][0]) #indica que quero saber a primeira coisa (indice 0) da ultima coisa que inseri (['opa', 90])
print(lista[-1]) #[opa, 90]
print(lista[5][3]) #lista 5 indice 3 (8)

matriz = [
     [ 0, 1, 2 ], #0 - l1
     [ 3, 4, 5 ], #1 - l2
     [ 6, 7, 8 ]  #2 - l3
#      0  1  2
#     c1  c2  c3   
]

print('tamanho de linhas matriz:', len(matriz)) #O len(comprimento) serve para contar quantos elementos existem em uma lista (ou em cada linha da matriz). 
#len(matriz) → retorna 2, porque a matriz tem 2 linhas.
#len(matriz[0]) → retorna 3, porque a primeira linha tem 3 elementos (colunas).

soma = 0
for linha in range(len(matriz)): #para linha no intervalo de 3(pq tem 3 linhas)
    for coluna in range(len(matriz[linha])):# Quando linha = 0 → matriz[0] = [0, 1, 2] (tem 3 colunas). Quando linha = 1 → matriz[1] = [3, 4, 5] (também 3 colunas).
        #len(matriz[linha]) → conta quantas colunas tem naquela linha.Sempre vai dar 3 nesse exemplo.
        #len(matriz) → conta quantas linhas tem. len(matriz[linha]) → conta quantas colunas tem em cada linha. Os dois for servem para percorrer linha por linha, coluna por coluna.
        soma += matriz[linha][coluna]

print(soma)
print(matriz[1][2])
