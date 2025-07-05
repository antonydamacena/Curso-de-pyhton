print('')
print('\033[1;30m' + '=-=' * 20 + '\033[m')
print('\033[0;33m🛒 SUPERMERCADO IRMÃOS PEIXOTOS 🛒\033[m')
print('\033[1;30m' + '=-=' * 20 + '\033[m\n')

# Verificando valor do produto

valor = float(input('Qual a valor do produto? '))

# Verificando condição de pagamento:

print('''Bom dia, senhor(a)! Qual será a forma de pagamento?
💰 Digite 0 para dinheiro/cheque (10% de desconto)
💳 Digite 1 para à vista no cartão (5% de desconto)
💳 Digite 2 para parcelamento em 2x no cartão
💳 Digite 3 para parcelamento em 3x ou mais no cartão (20% de juros)''')

payment_method = int(input("Escolha a opção desejada: "))

# Aplicação das condições
if payment_method == 0:
    print(f"Tudo certo! O Senhor(a) receberá um desconto de 10%, pagando apenas R${valor - (valor * 0.10):.2f}.")
elif payment_method == 1:
    print(f"Tudo certo! O Senhor(a) receberá um desconto de 5%, pagando apenas R${valor - (valor * 0.05):.2f}.")
elif payment_method == 2:
    print(f"Tudo certo! O valor total foi R${valor:.2f}.")
elif payment_method == 3:
    print(f"Tudo certo, o Senhor(a) terá um acréscimo de 20% de juros, pagando um total de R${valor + (valor * 0.20):.2f}.")
else:
    print("Opção inválida! Por favor, escolha uma opção correta.")

