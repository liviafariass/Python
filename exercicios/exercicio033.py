#Peça um número e diga se ele é primo ou não.
n = int(input('Insira um número: '))
d = int('3', '5', '7')

if n % d != 0:
    print('Esse é um número primo.')

else:
    print('Esse número não é primo')