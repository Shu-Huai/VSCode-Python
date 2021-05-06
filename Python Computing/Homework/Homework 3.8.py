primeNumber = [1, 2, 3, 4]
formedNumber = []
for i in range(0, len(primeNumber)):
    primeNumber[i], primeNumber[0] = primeNumber[0], primeNumber[i]
    for j in range(1, len(primeNumber)):
        primeNumber[j], primeNumber[1] = primeNumber[1], primeNumber[j]
        for h in range(2, len(primeNumber)):
            primeNumber[h], primeNumber[2] = primeNumber[2], primeNumber[h]
            formedNumber.append(int(str(primeNumber[0]) + str(primeNumber[1]) + str(primeNumber[2]) + str(primeNumber[3])))
            primeNumber[h], primeNumber[2] = primeNumber[2], primeNumber[h]
        primeNumber[j], primeNumber[1] = primeNumber[1], primeNumber[j]
    primeNumber[i], primeNumber[0] = primeNumber[0], primeNumber[i]
resultNumber = []
for number in formedNumber:
    for i in range(2, number):
        if not number % i:
            break
    else:
        resultNumber.append(number)
print("The result is: ", end="")
for i in range(len(resultNumber)):
    print(resultNumber[i], end="")
    if i != len(resultNumber) - 1:
        print(", ", end="")
print(".\n", end="")