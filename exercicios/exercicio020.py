lista_de_compras = [
    ('camiseta', 19.98),      #0 - lista
    ('calca jeans', 100.00),  #1 - lista
    ('meia g', 7.99)          #2 - lista
      #0 - tupla #1 - tupla    
]
total = 0

for item in lista_de_compras:
    total += item[1] #pq item[1]? pq ali nas tuplas, o nome camiseta, calca jeans e meia g estao no indice 0, e os precos estao no indice[1]. E como queremos a soma somente dos valores, iremos atribuir ao total o valor de cada item do indice [1], que sera somente os precos

print(f'Total da compra: {total}')

indice = 0 # pq desse indice? pq o while n percorre a lista sozinho igual o for, entao ele precisa de um indice que mostre o inicio da lista. E em python, o peimeiro indice da lista comeca com 0 = ('camiseta', 19.98)
total_de_compras = 0 

while indice < len(lista_de_compras): #traducao dessa linha: Enquanto o indice for menor que 3, continue somando os preços.Quando indice chegar a 3, a condição não será mais verdadeira, e o loop termina.
    total_de_compras += lista_de_compras[indice][1] #o total vai receber um novo valor que vai ser a lista no indice = 0 = ('camiseta', 19.98) e dentro dessa tupla vai pegar somente o indice 1 = 19,98 (o valor que queremos para saber o total da compra)
    indice += 1

print(f'O total de compras: {total_de_compras}')

# como diferenciar os indices?

#Índice da lista → qual linha/item da lista você quer acessar (0, 1, 2...) ex: lista = [1,2,3] quero acessar o indice 1 = 2

#Índice da tupla → qual elemento dentro do item/tupla você quer (0 = nome, 1 = preço) ex: tupla = ('camiseta', '19.98') quero acessar o indice 1 = '19.98'