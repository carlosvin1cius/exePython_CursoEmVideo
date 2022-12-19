print("===== EXERCICIO 025 =====")
nome = input("Digite seu nome: ")
nome = nome.upper()
res = "SILVA" in nome
# res = res.replace("TRUE", "VERDADEIRO")
# res = res.replace("FALSE", "FALSO")
print("O nome {} Contem a palavra 'silva'?: {}".format(nome, res))
