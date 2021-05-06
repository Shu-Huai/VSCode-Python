from random import randint

numberList = [randint(-65536, 65536) for i in range(50)]
i = len(numberList) - 1
for i in range(len(numberList) - 1, -1, -1):
    if numberList[i] % 2:
        del numberList[i]
print("The list is:")
print(numberList)