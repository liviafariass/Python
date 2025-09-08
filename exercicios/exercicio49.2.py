#exercicio 49 de forma simplificada
#definicao funcoes auxiliares, constantes            
opcoes = {
    '1': lambda x,y: x + y,
    '2': lambda x,y: x - y,
    '3': lambda x,y: x * y,
    '4': lambda x,y: x / y,
    '5': lambda x,y: exit() 
}
    
def menu():#definir a funcao principal    
    while True:
            n1 = float(input('Insira um número: '))
            n2 = float(input('Insira um número: '))

            print('Digite a opção desejada:\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Sair')

            op = input('')

            if op in opcoes.keys():
                print(opcoes[op](n1,n2))
            else:
                print('Opção Inválida')
    
if __name__ == '__main__': #diretiva para execucao da funcao principal ao executar o arquivo
    menu()