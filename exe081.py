from pickle import TRUE


print("===== EXERCICIO 081 ====")
lista = []
while True:
    res= ""
    n = int(input("DIGITE UM VALOR: "))
    lista.append(n)
    res = str(input("QUER CONTINUAR? [S/N]: "))[0]
    if res in "Nn":
        break
lista.sort(reverse=True)
print(f"Você digitou {len(lista)} elementos")
print(f"Ordem decrescente:{lista}")
if 5 in lista:
    print("O VALOR 5 APARECE NA LISTA.")
else:
    print("O VALOR 5 NÃO ESTA NA LISTA.")
