x = input("Digite algo: ")
print("O tipo primitivo desse valor é: ", type(x))
print("Só tem espaços? ", x.isspace()) #isspace = verifica se o valor é um espaço
print("É um número? ", x.isnumeric()) #isnumeric = verifica se o valor é um número
print("É alfabético? ", x.isalpha()) #isalpha = verifica se o valor é um alfabético
print("É alfanumérico? ", x.isalnum()) #isalnum = verifica se o valor é alfanumérico
print("Está em maiúsculas? ", x.isupper()) #isupper = verifica se o valor está em maiúsculas
print("Está em minúsculas? ", x.islower()) #islower = verifica se o valor está em minúsculas
print("Está capitalizada? ", x.istitle()) #istitle = verifica se o valor está capitalizado, ou seja, se a primeira letra é maiúscula e as demais são minúsculas