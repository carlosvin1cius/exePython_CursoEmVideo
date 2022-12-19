print("===== EXERCICIO 026 =====")
frase = str(input("DIGITE UMA FRASE QUALQUER: ")).strip()
frase = frase.upper()
print("A letra 'A' aparece na frase: {} vezes".format(frase.count("A")))
print("A letra 'A' aparece pela primeira vez na posição {}".format(frase.find("A")+1))
print("A letra 'A' aparece por ultimo na posição {}".format(frase.rfind("A")+1))


