idade = int(input('Insira a sua data de nascimento:'))

if idade <= 1964:
    print('Voce pertence a geração Baby Boomer')
elif idade <= 1979:
    print('Voce pertence a geração X')
elif idade <= 1994:
    print('Voce pertence a geração Y')
elif idade <= 2025:
    print('Voce pertence a geração Z')
else:
    print('Voce não pertence a nenhuma geração.')