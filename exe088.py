import random
from time import sleep
resp = int(input("QUANTOS JOGOS ERÃO GERADOS?: "))
nums = list()
print("-"*20)
print("GERANDO NUMEROS...")
for i in range(1, resp+1):
    nums.append(random.sample(range(1, 60), 6))
for i in nums:
    i.sort()
    sleep(0.5)
    print(i)
print("-"*20)
print("BOA SORTE!")