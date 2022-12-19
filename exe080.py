print("==== EXERCICIO 080 =====")
n = list()
for i in range(0, 5):
    num = int(input("DIGITE UM NUMERO: "))
    if i == 0 or num > n[len(n)-1]:
        n.append(num)
    else:
        pos = 0
        while pos < len(n):
            if num <= n[pos]:
                n.insert(pos, num)
            break
            pos +=1
print(n)