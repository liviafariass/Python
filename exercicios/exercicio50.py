#import random
#random.randint(1,4) pega um numero inteiro aleatorio entre 1 e 4
import modulo #usa pra tudo do modulo
#from modulo import PI, saudacao -- usa pra algum especifico dentro do modulo, nao todos. Nao precisa do 'modulo.', so o (PI)

def soma(*args):
    soma = 0
    for num in args:
        soma += num
    return soma

print(modulo.PI)
print(modulo.saudacao())
print(modulo.soma(2, 4))
print(soma(2, 4, 6, 8))

print(__name__) #__main__ : todo arquivo .py tem uma variável especial chamada __name__. Se importarmos o arquivo como módulo em outro código, o __name__ dele será o nome do arquivo (sem .py)
print(modulo.__name__)

if __name__ == '__main__':
    print(soma(2, 4, 6, 8))