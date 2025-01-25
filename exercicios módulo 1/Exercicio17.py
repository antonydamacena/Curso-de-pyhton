# Exercicio 17 Hypotenusa 🙄
from math import hypot
ca= int(input('Para caucularmos a valor da hipotenusa do seu triangullo retangulo, diga-me o valor do sseu cateto adjacente: '))
co= int(input('E agora de seu cateto adjacente:'))
print (f' Sendo o seu cateto adjacente {ca} e seu cateto oposto {co} a sua hipotenusa é {hypot(ca,co)}')