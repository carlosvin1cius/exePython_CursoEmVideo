from operator import itemgetter
from random import randint
valores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
           'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ranking = ()
for k, v in valores.items():
    print(f'O {k} tirou {v}')
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
print("-="*30)
print("RANKING:")
for i, v in enumerate(ranking):
    print(f'{i+1}° LUGAR: {v[0]} com {v[1]}')
