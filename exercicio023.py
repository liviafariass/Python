while True: #enquanto for verdade:
    op = input('Digite a opção desejada:\n1- Saudação\n2- Sair\n3- Nenhuma das anteriores\n') #opcoes

    if op == '1': #se opcao for 1:
        print('Uma saudação qualquer') #escreva: uma saudacao qualquer
    elif op == '2': #se nao se opcao for 2:
        break #pause
    elif op == '3': #se nao se opcao for 3:
        continue
    else: #se nao 
        print('Opção inválida') #escreva opcao invalida

print('fim')