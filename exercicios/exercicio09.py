peso = float(input('Insira o seu peso:'))
altura = float(input('Insira a sua altura:'))
imc = peso / (altura**2)

if imc < 18.5:
    print(f'Baixo peso - IMC: {imc:.2f}')
elif imc < 24.9:
    print(f'Peso normal - IMC: {imc:.2f}')
elif imc < 29.9:
    print(f'Pré obesidade - IMC: {imc:.2f}')
elif imc < 34.9:
    print(f'Obesidade grau I: - IMC: {imc:.2f}')
elif imc < 39.9:
    print(f'Obesidade grau II - IMC: {imc:.2f}')
else:
    print(f'Obesidade grau III - IMC: {imc:.2f}')           