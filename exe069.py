print("===== EXERCICIO 069 =====")
agemais = men = femmenos = 0
while True:
    sex = r = " "
    print("="*20)
    print("CADASTRO DE PESSOAL:")
    print("="*20)
    age = int(input("DIGITE SUA IDADE: "))
    while sex not in "MF":
        sex = str(input("DIGITE SEU SEXO? [M/F} ")).strip().upper()
    print("-"*20)
    if age >= 18:
            agemais += 1
    if sex == "M":
        men += 1
    if sex == "F" and age < 20:
        femmenos += 1
    while r not in "SN":
        r = str(input("DESEJA CONTINUAR? [SIM: S / NÃO: N] ")).strip().upper()
    if r in "NÃONAON":
        print("DADOS CADASTRADOS.")
        break
print("="*20)
print(f"{agemais} TEM MAIS DE 18  ANOS")
print(f"{men} HOMENS FORAM CADASTRADOS")
print(f"{femmenos} MULHERES COM MENOS DE 20 ANOS")
