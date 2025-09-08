from colorama import init, Fore, Back, Style
init(autoreset=True)

#def menu():
        
    
while True:
        print(Style.BRIGHT + Fore.MAGENTA +'---BANCO DE DADOS---')
        print('1- O que é um banco de dados?')
        print('2- Quais são os tipos de banco de dados?')
        print('3- O que é SQL?')
        print('4- Qual a diferença de SQL, MYSQL e NOSQL?')
        print('5- Sair')
        
        opcao = input('Escolhe um número acima:')
    
        if opcao == '1':
            print('\nUm banco de dados é um sistema organizado para guardar informações de forma estruturada, para que você consiga inserir, buscar, alterar e excluir dados de maneira rápida e fácil.\n')
            
        elif opcao == '2':
            print('\n1. Bancos de Dados Relacionais (SQL):\n')
            print('-- Organiza os dados em tabelas com linhas e colunas. ')
            print('--Utilizam a linguagem SQL (Structured Query Language) para gerenciar dados. ')
            print('\n2. Banco de Dados NoSQL:\n')
            print('--Não seguem o modelo tabular dos bancos de dados relacionais. ')
            print('--São flexíveis para dados não estruturados e em grande volume.')
        elif opcao == '3':
            print('\nSQL (Structured Query Language) é uma linguagem usada para conversar com bancos de dados relacionais. Ela serve para inserir, consultar, atualizar e excluir dados de forma organizada.\n')
        elif opcao == '4':
            print('\n1. SQL (Structured Query Language)\n')
            print('O que é: uma linguagem usada para consultar e manipular bancos de dados relacionais.')
            print('Função: serve para criar tabelas, inserir, atualizar, apagar e consultar dados.')
            print('\n2. MySQL')
            print('O que é: um sistema de gerenciamento de banco de dados (SGBD) que usa SQL.')
            print('Função: armazena dados de forma relacional (em tabelas) e permite manipulá-los usando SQL.\n')
            print('\n3. NoSQL\n')
            print('O que é: um tipo de banco de dados não-relacional.')
            print('Função: armazena dados de forma flexível, como documentos, chave-valor, grafos ou colunas largas.')
        else:
            res = input('Deseja mesmo sair?')
            if res != 'sim'.capitalize():
                break
            
            