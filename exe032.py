print("===== EXERCICIO 032 =====")
from datetime import date
ano = int(input("DIGITE O ANO: o digito [0] representa o ano atual: "))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print("O ano {} é comum.(365 dias!)".format(ano))
