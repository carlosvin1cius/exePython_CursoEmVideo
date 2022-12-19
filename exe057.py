print("===== EXERCICIO 057 =====")
sexo = str(input("DIGITE SEU SEXO [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("DADOS INVALIDOS: INFORME NOVAMENTE: [M/F] ")).strip().upper()[0]
print("Opção valida")