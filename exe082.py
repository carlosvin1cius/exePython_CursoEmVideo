lista = []
par = []
impar= []
while True:
    res = " "
    n = int(input("DIGITE UM VALOR: "))
    res = str(input("DESEJA CONTINUAR? [S/N] ")).strip()
    lista.append(n)
    if n %2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if res in "Nn":
        break
print(lista)
print(f"Pares: {par}")
print(f"Impares: {impar}")
