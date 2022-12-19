from tkinter import N


print("==== EXERCICIO 064 =====")
count = n = s = 0
while n != 999:
    n = int(input("DIGITE UM NUMERO: [999 pra parar o programa] "))
    s = s+n
    count += 1
    if n == 999:
        s = s-n
        count -= 1
        print("PROGRAMA FINALIZADO!")
print("{} números foram digitados, a soma entre todos é {}".format(count, s))