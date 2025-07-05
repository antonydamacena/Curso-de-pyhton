from datetime import date

# 🎖️ Simulador de Alistamento Militar
print("\n⚔️  EXÉRCITO NACIONAL - CHAMADO AO DEVER ⚔️")
print("=" * 50)

# 📅 Entrada de dados
ano_nascimento = int(input("\n📝 Digite o ano de seu nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print("\n🔎  Analisando sua situação...\n")

# ⚔️  Verifica a idade para o alistamento
if idade == 18 or idade == 17:
    print("\033[1;31m🔥 SOLDADO, CHEGOU SUA HORA! 🚀\033[m")
    print("📌 Você está apto para o alistamento militar. Prepare-se para o treinamento intenso!")
elif idade < 18:
    anos_faltando = 18 - idade
    print(f"\033[1;33m⌛ Ainda não está na hora de servir! 😫\033[m")
    print(f"📌 Faltam \033[1;36m{anos_faltando}\033[m anos para seu alistamento. Estaremos esperando ansiosos! 💪")
else:
    anos_atrasado = idade - 18
    print("\033[1;31m⚠️ SOLDADO, VOCÊ ESTÁ ATRASADO! 😡\033[m")
    print(f"📌 Seu alistamento deveria ter ocorrido há \033[1;36m{anos_atrasado}\033[m anos.")
    print("🔥 Prepare-se para exercícios pesados e treinos especiais! Você não vai escapar! 💪😈")

# 🎖️ Mensagem final
print("\n🏆 O Exército Nacional conta com você! Seja forte, treine duro e esteja pronto para desafios! ⚔️💙")
print("=" * 50)
