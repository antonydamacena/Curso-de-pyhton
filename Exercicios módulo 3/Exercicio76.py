produtos = (
    'caneta', 3.50,
    'lapiseira', 5.99,
    'mochila', 129.90,
    'fichário', 42.75,
    'marcador', 7.10,
    'agenda', 18.80,
    'borracha', 1.90,
    'caderno', 24.50,
    'régua', 4.60,
    'estojo', 12.25
)
for i in range (0,len(produtos)):
    if i %2 == 0:

        print(f'{(produtos[i]).capitalize():.<30}',end=''*12)
    else:
        print(f'R${(produtos[i]): >2.2f}')