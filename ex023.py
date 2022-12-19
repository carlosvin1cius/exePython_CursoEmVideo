print("===== EXERTCICIO 023 =====")
import random
# num = random.random(1, 9999)
num = int(input("Digite um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
mil = num // 1000 % 10
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(mil))
