# 📚 Sistema de Avaliação Escolar
print("\n📖 Bem-vindo ao Colégio Opção! 📖")
print("=" * 40)

# 👩‍🏫 Apresentação
print("\033[1;30;40mBom dia! Eu sou a diretora Enilde e hoje irei avaliar seu desempenho escolar.\033[m")

# 📝 Entrada de notas
nota1 = int(input("\n✏️  Qual foi sua nota na \033[4mprimeira\033[m avaliação? "))
nota2 = int(input("✏️  Qual foi sua nota na \033[4msegunda\033[m avaliação? "))
nota3 = int(input("✏️  Qual foi sua nota na \033[4mterceira\033[m avaliação? "))

# 🧮 Cálculo da média
media = (nota1 + nota2 + nota3) / 3

print("\n📊 Calculando sua média...\n")
print(f"🎯 Sua média final é: \033[1;32m{media:.2f}\033[m\n")

# 🎓 Classificação do desempenho
if media < 5:
    print("\033[1;31m❌ INFELIZMENTE, você está REPROVADO!\033[m\n")
    print("📌 Continue estudando e se dedicando. Você é capaz de melhorar!")
elif 5 <= media < 7:
    print("\033[1;33m⚠️ Você está de RECUPERAÇÃO!\033[m\n")
    print("📌 Ainda há uma chance! Revise seus conteúdos e se prepare bem para a prova final.")
else:
    print("\033[1;32m✅ PARABÉNS! Você foi APROVADO! 🎉\033[m\n")
    print("📌 Continue focado nos estudos e siga brilhando! 🚀")

# 🌟 Mensagem final
print("\n🏫 O aprendizado nunca para! Continue estudando e se esforçando. 📚💡\n")
