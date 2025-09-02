def soma_multiplos_valores(*numeros): # o * significa que pode ter infinitos numeros dentro // transforma em tupla // args 
    soma = 0
    for num in numeros:
        soma += num 
    return soma

def soma_kwargs(**kwargs):#retorna a funcao em dicionario// keyword arguments
    print(type(kwargs))