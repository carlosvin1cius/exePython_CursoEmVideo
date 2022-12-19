print("===== EXERCICIO 008 =====")
metros = float(input("Digite a medida em metros: "))
# km = metros/1000
# hm = metros/100
# dam = metros/10
# dm = metros/(metros*10)
# cm = metros/(metros*100)
# mm = metros/(metros*1000)
# print("{}Km\n{}Hm\n{}Dam\n{:.0f}Dm\n{:.0f}Cm\n{:.0f}Mm".format(km, hm, dam, dm, cm, mm))
print("{}Km\n{}Hm\n{}Dam\n{:.0f}Dm\n{:.0f}Cm\n{:.0f}Mm".format(metros/1000, metros/100, metros/10, metros*10, metros*100, metros*1000))

