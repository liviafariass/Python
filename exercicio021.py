lista_de_compras = [
    ('Camiseta', 19.90),
    ('calca jeans', 20.50),
    ('meia g', 6.90),
    ('camiseta', 10.00)
]
#totalizar o carrinho aplicando 10% de desconto somente na camiseta

total = 0
desconto = 0.9 #valor x 0.9 = 10% de desconto

for compra in lista_de_compras:
    if compra[0].upper() == 'CAMISETA':
        total += compra[1] * desconto
    else:
        total += compra[1]

print (f'Valor total de compras aplicando o desconto: {total:.2f}')
