#acessos a dicionarios
dic = {
    'nome': 'Livia',
    'idade': 16,
    'dados': [0,1,2,3,4],
    'tupla': (7,8,9,10)
}

print(dic['tupla'][-1])
print(dic['tupla'])

for chave in dic.keys():
    if chave == 'idade':
        print(f'achei -', dic[chave])

for valor in dic.values():
    if valor == 'Livia':
        print('achei o nome')

for chave, valor in dic.items():
    print(f'key: {chave} - value: {valor}')
