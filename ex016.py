print("===== EXERCICIO 016 =====")
from math import sqrt
n = float(input("DIGITE UM NUMERO E MOSTRAREMOS SUA PORÇÃO INTEIRA: "))
raiz = sqrt(n)
print("A raiz de {} é: {} e sua porção inteira é {:.0f}".format(n, raiz, raiz))
