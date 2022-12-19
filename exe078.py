nums = list()
maiorpos = list()
menorpos = list()
maior = menor = 0
for i in range (0, 5):
    nums.append(int(input("DIGITE UM VALOR: ")))
    if i == 0:
        maior = menor = nums[i]
    elif maior <= nums[i]:
        maior = nums[i]
    elif menor > nums[i]:
            menor = nums[i]
print(f"O maior numero é {maior}, esta localizado na posição: ", end="")
for i, v in enumerate(nums):
    if v == maior:
        print(f"{i}", end=" ")
print()
print(F"O menor numero é {menor}, esta localizado na posição: ", end="")
for i, v in enumerate(nums):
    if v == menor:
        print(f"{i}", end=" ")
print()
