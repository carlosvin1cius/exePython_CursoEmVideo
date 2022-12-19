print("===== EXERCICIO 068 =====")
while True:
    n = int(input("QUAL TABUADA VOCE DESEJA CONSULTAR? [0 ou negativo - FINALIZAR] "))
    if n <= 0:
        break
    for c in range (1, 11):
        mult = n*c
        print(f"{n} x {c} = {mult}")
    c += 1
print("FINALIZADO")