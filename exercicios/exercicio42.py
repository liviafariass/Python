dici = {}

while True:    
    print('--ESCOLHA UMA OPCAO ABAIXO--')
    print('1- Nome')
    print('2- Idade')
    print('3- CEP')

    opcao = input('Insira o número da opçao acima:')

    if opcao == '1':
        dici['nome'] = input('Insira o seu nome: ')
        resposta = input('Deseja continuar?')
        if resposta.upper() == 'SIM':
            continue
        else:
            break    
    elif opcao == '2':
        dici['idade'] = input('Insira a sua idade: ')
        resposta = input('Deseja continuar?')
        if resposta.upper() == 'SIM':
            continue
        else:
            break
    else:
        dici['cep'] = input('Insira o seu CEP: ')
        break
        
resposta = input('Deseja ver todos os valores inseridos?')
if resposta.upper() == 'SIM':
    print(dici) 