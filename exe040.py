print("===== EXERCICIO 040 =====")
nota1 = float(input("DIGITE SUA PRIMEIRA NOTA: "))
nota2 = float(input("DIGITE SUA SEGUNDA NOTA: "))
media = (nota1+nota2)/2
if media < 5.0:
    print("Sua média foi: {}, e você esta REPROVADO!".format(media))
elif 5.0 <= media <= 6.9:
    print("Sua média foi: {}, e você está de RECUPERAÇÃO!".format(media))
else:
    print("Sua média foi: {}, e você está APROVADO!".format(media))
