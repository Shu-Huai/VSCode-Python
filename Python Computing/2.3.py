from random import randint

randList = [randint(0, 100) for i in range(1000)]
randSet = set(randList)
formatCount = 0
for number in randSet:
    print("%3d: %3d times\t" % (number, randList.count(number)), end="")
    if not (formatCount + 1) % 5:
        print("\n", end="")
    formatCount += 1
print("\n", end="")
