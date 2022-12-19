print("===== EXERCICIO 039 =====")
from datetime import date
nasc = int(input("DIGITE O ANO DO DO SEU NASCIMENTO: "))
anoatual = date.today().year
idade = anoatual - nasc
if idade == 18:
    print("QUEM NASCEU EM {}, TEM {} E DEVE SE ALISTAR ESTE ANO!".format(nasc, idade))
elif idade < 18:
    print("QUEM NASCEU EM {}, TEM {} E FALTAM APENAS {} ANO PARA SE ALISTAR!".format(nasc, idade, (nasc + 18) - anoatual))
else:
    print("QUEM NASCEU EM {}, TEM {} E SE ALISTOU EM {}".format(nasc, idade, nasc + 18))

