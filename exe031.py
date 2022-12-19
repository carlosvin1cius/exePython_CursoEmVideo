print("===== EXERCICIO 031 =====")
km = int(input("Digite a distancia da viagem a ser feita: "))
if km <= 200:
    valorviagem = 0.50*km
    print("O valor da viagem a ser feita é de: R${}".format(valorviagem))
else:
    valorviagem = 0.45*km
    print("O valor da viagem a ser feita é de: R${}".format(valorviagem))
