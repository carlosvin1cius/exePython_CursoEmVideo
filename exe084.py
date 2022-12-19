pessoas = list()
dados = list()
maiorp = menorp = 0
while True:
    resp = " "
    dados.append(str(input("NOME: ")).upper())
    dados.append(float(input("PESO[KG]: ")))
    pessoas.append(dados[:])
    if len(pessoas) == 0:
        maiorp = dados[1] 
        menorp = dados[1]
    if maiorp < dados[1]:
            maiorp = dados [1]
    if menorp > dados[1]:
            menorp = dados[1]
    dados.clear()
    while resp not in "SsNn":
        resp = str(input("DESEJA CONTINUAR: [S/N] ")).upper().split()[0]
    if resp in "Nn":
        print("FINALIZADO")
        break
print("-="*20)
print(pessoas)
print(f"TOTAL CADASTRADOS: {len(pessoas)}")
print("PESSOAS MAIS PESADAS: ",end="")
for i in pessoas:
    if i[1] == maiorp:
        print(f"{i[0]}", end=" ,")

print(f"\nPESSOAS MENOS PESADAS: ", end="")
for i in pessoas:
    if i[1] == menorp:
        print(f"{i[0]}", end=" ,")
