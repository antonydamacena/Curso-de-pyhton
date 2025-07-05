from datetime import date
from time import sleep
# 🎯 Classificação de nadadores para competição
print("\n🏅 🔵 Classificação de Natação 🔵 🏅\n")

# 📌 Entrada de dados
ano = int(input("📅 Em que ano você nasceu? "))
today = date.today().year
idade = today - ano

print("\n🔍 Analisando sua categoria...\n")
sleep(2)
# 🏊‍♂️ Definição das categorias
if idade <= 9:
    print("\033[1;34m🐠 Categoria MIRIM - Pequenos nadadores iniciantes!\033[m")
elif idade <= 14:
    print("\033[1;36m🐬 Categoria INFANTIL - Jovens promessas da natação!\033[m")
elif idade <= 19:
    print("\033[1;32m🐳 Categoria JÚNIOR - Nadadores em desenvolvimento para o alto nível!\033[m")
elif idade == 20:
    print("\033[1;33m🏊 Categoria SÊNIOR - Atletas experientes, prontos para grandes desafios!\033[m")
else:
    print("\033[1;31m🔥 Categoria MASTER - Grandes talentos da natação com experiência consolidada!\033[m")

# 🌊 Mensagem final
print("\n🌟 Continue treinando forte e conquiste novos recordes! 🏆💙\n")
