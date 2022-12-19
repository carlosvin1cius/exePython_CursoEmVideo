print("===== EXERCICIO 020 =====")
import random
aluno1 = input("DIGITE O NOME DO PRIMEIRO ALUNO: ")
aluno2 = input("DIGITE O NOME DO SEGUNDO ALUNO: ")
aluno3 = input("DIGITE O NOME DO TERCEIRO ALUNO: ")
aluno4 = input("DIGITE O NOME DO QUARTO ALUNO: ")
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print("ORDEM DE APRENSENTAÇÃO:\n{}".format(lista))
