from audioop import reverse
from typing import Reversible


print("===== EXERCICIO 53 ======")
frase = (input("DIGITE UMA FRASE: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = ""
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Palindromo.")
else:
    print("Não é palindromo.")
