#dados imutaveis, nao da pra alterar
#tupla = (0,1,2,3)
#tupla += (4,5,6,7) #aqui foi criada uma nova tupla com os valores da tupla antiga
#print(tupla)
#string = ''
#inteiros = 1
#float = 10.5

#x +=1 -> x = x+1

#dados mutaveis, da pra alterar
listas = [0, 1, 2, 'oii']
#dic = {}
#dic ['nova_chave'] = 1

def adiciona_item(listas, item):
    listas.append(item)
    
adiciona_item(listas, 'macarrao')
print(listas)

adiciona_item(listas, 'feijao')
print(listas)