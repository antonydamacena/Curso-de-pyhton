# 🔺 Analisador de Triângulos 🔺
print("\n📏 Verificador de Triângulos\n")

# 📌 Entrada de dados
reta1 = float(input("➡ Digite o valor da primeira reta: "))
reta2 = float(input("➡ Digite o valor da segunda reta: "))
reta3 = float(input("➡ Digite o valor da terceira reta: "))

print("\n📊 Analisando os segmentos...\n")

# 🔍 Verifica se os segmentos podem formar um triângulo
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:

    # 🎭 Identifica o tipo de triângulo
    if reta1 == reta2 == reta3:
        print("\033[1;32m✅ Os segmentos formam um TRIÂNGULO EQUILÁTERO!\033[m")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("\033[1;33m🔶 Os segmentos formam um TRIÂNGULO ISÓSCELES!\033[m")
    else:
        print("\033[1;34m🔷 Os segmentos formam um TRIÂNGULO ESCALENO!\033[m")
else:
    print("\033[1;31m❌ Os segmentos NÃO podem formar um triângulo!\033[m")

# 🌟 Mensagem final
print("\n✨ Continue explorando a matemática dos triângulos! 😉\n")
