print("===== EXERCICIO 051 =====")
ntermo = int(input("DIGITE O PRIMEIRO TERMO: "))
pa = int(input("DIIGTE A PROGRESSÃO DESTE TERMO: "))
decimo = ntermo + (10 - 1) * pa
print("OS DEZ PRIMEIROS TERMOS A PARTIR DE {} PROGREDINDO ARITMETICAMENTE EM {} É:".format(ntermo, pa))
for c in range(ntermo, decimo + pa, pa):
    print("{}".format(c), end=" ->")
print("Fim")