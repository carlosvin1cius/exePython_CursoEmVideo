print("===== EXERCICIO 036 =====")
nome = str(input("OLÁ:\nDIGITE SEU NOME PARA COMEÇARMOS: ")).upper()
valorcasa = float(input("{}, DIGITE O VALOR DA CASA: R$".format(nome)))
salario = float(input("{}, AGORA DIGITE SEU SALARIO: R$".format(nome)))
anos = int(input("{} EM QUANTOS ANOS SERA O PAGAMENTO DA CASA: ".format(nome)))
prestação = valorcasa/(anos*12)
if prestação <= salario * 30 / 100:
    print("{}, O VALOR DO NOSSO EMPRESTIMO FOI APRAVODO!\nPARCELAS FIXAS DE R${:.2f}".format(nome, prestação))
else:
    print("{} INFELIZMENTE AS PARCELAS DE R${:.1f} SÃO MAIORES QUE 30% DO SEU SALARIO\nEMPRESTIMO NÃO APROVADO!".format(nome, prestação))
