print("===== EXERCICIO 029 =====")
kmh = int(input("DIGITE A VELOCIDADE DO CARRO NA AUTOVIA: "))
if kmh > 80:
    print("Você recebeu uma multa de velocidade!")
    multa = (kmh-80)*7
    print("Por estar andando a {}km/h, {}km/h acima da velocidade do limite da via, o valor da multa sera de: R${}".format(kmh, kmh-80, multa))
else:
    print("Você esta dentro do limite de velocidade!")
