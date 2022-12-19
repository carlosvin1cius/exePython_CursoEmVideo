print("===== EXERCICIO 010 =====")
din = float(input("Digite o quanto de dinheiro você possui: R$"))
euro = din/5.21
dolar = din/5.18
print("Voce pode comprar com R${} uma quantia em:\nDolar: ${:.2F}\nEuro: ${:.2f}".format(din, dolar, euro))
