# 💪 Cálculo do Índice de Massa Corporal (IMC)
print("🔍 Calculadora de IMC 🔍\n")

# 📌 Entrada de dados
peso = float(input("⚖️ Qual é o seu peso (kg)? "))
altura = float(input("📏 Qual é a sua altura (m)? "))

# 🧮 Cálculo do IMC
imc = peso / (altura ** 2)

# 🎯 Exibição do resultado formatado
print(f"\n🔹 Seu IMC é: \033[1;32m{imc:.2f}\033[m\n")

# 🏆 Classificação do IMC
print("📊 Classificação do IMC:")

if imc < 18.5:
    print("\033[1;34m➡ Você está abaixo do peso ideal!\033[m")
elif 18.5 <= imc < 25:
    print("\033[1;32m✅ Você está no peso ideal!\033[m")
elif 25 <= imc < 30:
    print("\033[1;33m⚠️ Você está com sobrepeso!\033[m")
elif 30 <= imc < 40:
    print("\033[1;31m❗ Você está com obesidade!\033[m")
else:
    print("\033[1;41m🚨 Você está com obesidade mórbida!\033[m")

# 📢 Mensagem final
print("\n💡 Mantenha um estilo de vida saudável! Pratique exercícios e tenha uma alimentação equilibrada. 😉")
