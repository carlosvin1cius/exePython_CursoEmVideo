print("===== EXERCICIO 058 =====")
from random import randrange
c = 1
pcn = randrange(0,11)
usern = int(input("Tente acertar o numero do computador: "))
while usern != pcn:
    usern = int(input("Voce digitou o numero {} diferente do computador, tente novamente: ".format(usern, pcn)))
    c += 1
print("Você ACERTOU. Digitou {} e o computador: {}, parabéns".format(usern, pcn))
print("TOTAL DE TENTATIVAS: {}".format(c))
