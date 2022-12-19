print("===== EXERCICIO 074 =====")
from random import randrange
maior = menor = 0
ntupla = (randrange(1, 10), randrange(1, 10), randrange(1, 10), randrange(1, 10), randrange(1, 10))
print(f"TUPLA: {ntupla}")
print(f"O maior valor sorteado foi {max(ntupla)}\nO menor valor sorteado foi {min(ntupla)}")

'''for i in range(0, len(ntupla)):
    if i == 0:
        maior = ntupla[i]
        menor = ntupla[i]
    elif maior < ntupla[i]:
        maior = ntupla[i]
    if menor > ntupla[i]:
        menor = ntupla[i]
print(f"O MAIOR NUMERO: {maior}\nO MENOR NUMERO: {menor}")'''
