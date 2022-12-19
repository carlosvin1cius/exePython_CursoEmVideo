print("===== EXERCICIO 017 =====")
from math import pow, sqrt
ctop = float(input("DIGITE O COMPRIMENTO DO CATETO OPOSTO: "))
#print(pow(ctop, 2))
cadj = float(input("DIGITE O COMPRIMENTO DO CATETO ADJACENTE: "))
hip = sqrt(pow(ctop, 2) + pow(cadj, 2))
print("A soma dos quadrados dos catetos é de: {:.1f}".format(hip))

