def media(n1, n2, n3):
    return (n1 + n2 + n3)/3
n1 = 9
n2 = 9
n3 = 1

print(media(n1, n2, n3))

if media(n1, n2, n3) >= 6:
    print('Voce foi aprovado!')
else:
    print('Voce foi reprovado!')