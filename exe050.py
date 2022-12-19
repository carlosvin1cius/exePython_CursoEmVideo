print("===== EXERCICIO 040 =====")
s = 0
for c in range(1, 7):
    n = int(input("DIGITE UM NUMERO: "))
    if  n % 2 == 0:
        print("Numero par digitado e somado!")
        s = s+n
    else:
        print("Numero impar digitado e ignorado!")
print("A soma dos apres é {}".format(s))