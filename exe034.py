print("===== Exercicio 034 =====")
sal = float(input("DIGITE O VALOR DO SEU SALARIO EM R$: "))
if sal > 1250:
    nsal = sal + ((sal*10)/100)
    print("Seu novo salario é de: R${}".format(nsal))
else:
    nsal = sal + ((sal*15)/100)
    print("Seu novo salario é de: R${}".format(nsal))
