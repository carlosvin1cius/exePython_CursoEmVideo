print(("===== EXERCICIO 019 ====="))
import random
nome1 = input("DIGITE O NOME DO PRIMEIRO ALUNO: ")
nome2 = input("DIGITE O NOME DO SEGUNDO ALUNO: ")
nome3 = input("DIGITE O NOME DO TERCEIRO ALUNO: ")
nome4 = input("DIGITE O NOME DO QUARTO ALUNO: ")
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print("O escolhido foi: {}".format(escolhido))

