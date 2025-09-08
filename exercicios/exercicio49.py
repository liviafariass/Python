while True:
    n1 = float(input('Insira um número: '))
    n2 = float(input('Insira um número: '))

    print('Digite a opção desejada:\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Sair')

    op = input('')

    if op == '1':
        print('soma: ', n1+n2)
    elif op == '2':
        print('Subtração: ', n1-n2)
    elif op == '3':
        print('Multiplicação: ', n1*n2)
    elif op == '4':
        if n2 == 0:
            print('Não divisível por 0!')
        else:
            print('Divisão: ', n1/n2)
    elif op == '5':
        break
    else:
        print('Opção Inválida')