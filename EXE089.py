from time import sleep
boletim = list()
while True:
    nome = str(input("NOME DO ALUNO: ")).upper().strip()
    n1 = float(input("PRIMEIRA NOTA: "))
    n2 = float(input("SEGUNDA NOTA: "))
    media = (n1 + n2)/2
    boletim.append([nome, [n1, n2], media])
    resp = " "
    while resp not in "SsNn":
        resp = str(input("NOVO CADASTRO? [S/N] ")).split()[0]
    if resp in "Nn":
        print("FINALIZANDO...")
        sleep(0.6)
        break
print("-"*41)
print(f'{"NOME:":>4}{"MÉDIA ":>31}')
print("-"*41)

for c, i in enumerate(boletim):
    print(f'{c}° - {i[0]:<23} MÉDIA: {i[2]:>5}')
print("-"*41)
while True:
    resp2 = " "
    while resp2 not in "SsNn":
        resp2 = str(input("VERIFICAR NOTAS DE UM ALUNO ESPECIFICO? [S/N] ")).split()[0]
    if resp2 in "Ss":
        opc = int(input("DIGITE O INDICE DO ALUNO A SER REQUERIDO: "))
        if opc <= len(boletim) - 1:
            print("-"*41)
            print(f'{"NOME:":>4}{"MÉDIA ":>31}')
            print("-"*41)
            print(f"NOTAS DE {boletim[opc][0]}: {boletim[opc][1]}")
        else:
            print("Opção invalida!")
        if opc == 999:
            print("FINALIZANDO...")
            sleep(0.6)
            break
    if resp2 in "Nn":
        print("FINALIZANDO...")
        sleep(0.6)
        break
print("ATÉ LOGO")
