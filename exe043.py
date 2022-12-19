print("===== EXERCICIO 043 =====")
kg = float(input("QUAL O SEU PESO? (KG) "))
alt = float(input("QUAL A SUA ALTURA? (m) "))
imc = kg / (alt ** 2)
if imc <= 18.5:
    print("Seu IMC: {:.2f} esta na categoria ABAIXO DO PESO! (IMC: 18.5)".format(imc))
elif imc <= 25:
    print("Seu IMC: {:.2f} esta na categoria PESO IDEAL! (IMC ENTRE: 18.6 e 25)".format(imc))
elif imc <= 30:
    print("Seu IMC: {:.2f} esta na categoria SOBREPESO! (IMC ENTRE 25 e 30)".format(imc))
elif imc <= 40:
    print("Seu IMC: {:.2f} esta na categoria OBESIDADE! (IMC ENTRE 30 e 40)".format(imc))
else:
    print("Seu IMC: {:.2f} esta na categoria OBESIDADE MORBIDA! (IMC ACIMA DE 40)".format(imc))

    #OBESIDADE = 40 OBESIDADE MORBIDA > 40