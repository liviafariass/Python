mercado = {}

while True: 

    print('--MENU DO MERCADO--')
    print('1- Adicionar item e preço do item')
    print('2- Alterar o valor de um produto')
    print('3- Ver lista de produtos criados')
    print('4- Apagar item criado')
    print('5- Sair')

    opcao = int(input('Insira o dígito conforme o menu acima: '))

    if opcao == 1:
        produto = input('\nAdicione o nome do item: \n')
        valor = float(input('\nAdicione o valor do item: \n'))
        mercado[produto] = valor
        print(f'O item {produto} com o valor {valor} foi adicionado na lista!')

    elif opcao == 2:
        produto = input('\nAdicione o nome do item: \n')
        if produto in mercado:
            novo_valor = float(input('\nAdicione o novo valor do item: \n'))
            mercado[produto] = novo_valor
            print(f'O item {produto} com o novo valor {novo_valor} foi adicionado na lista!')
        else:
            print('Esse produto não existe na lista')

    elif opcao == 3:
        print('--Lista--')
        print(mercado)

    elif opcao == 4:
        print('--Lista--')
        print(mercado)
        apagar_produto = input('Insira o produto que deseja apagar: ')
        if apagar_produto in mercado:
            mercado.pop(apagar_produto)
            print(f'O produto {apagar_produto} foi removido com sucesso!')
        else:
            print('Esse produto não existe na lista')

    elif opcao == 5:
        print('Saindo do sistema...')
        break

    else: 
        print('COMANDO INVÁLIDO')