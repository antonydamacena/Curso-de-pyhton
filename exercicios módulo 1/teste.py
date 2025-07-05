peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura em metros? '))

# Cálculo correto do IMC
imc = peso / (altura ** 2)

print(f"Seu IMC é: {imc:.2f}")

# Classificação do IMC
if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')
