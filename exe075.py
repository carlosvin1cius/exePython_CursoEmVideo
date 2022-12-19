print("===== EXERCICIO 075 =====")
num = (int(input("DIGITE UM NUMERO: ")),
       int(input("DIGITE UM NUMERO: ")),
       int(input("DIGITE UM NUMERO: ")),
       int(input("DIGITE UM NUMERO: ")))
print(f"O numero 9 apareceu {num.count(9)} Vezes")
if 3 in num:
    print(f"O numero 3 aparece na posição: {num.index(3)+1}")
else:
    print(f"O numero 3 não aparece.")
print("pares: ", end="")
for i in num:
    if i % 2 == 0:
        print(i, end=", ")

