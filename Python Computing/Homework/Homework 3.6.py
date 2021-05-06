number = int(input("Please input a number: "))
print("%d" % number, end="")
if number >= 1000:
    exit()
if number == 1 or number == 0:
    print(" = %d × %d" % (number, number))
    exit()
formatTag = 0
while number > 1:
    for i in range(2, number + 1):
        if not number % i:
            if not formatTag:
                print(" = ", end="")
                formatTag = 1
            else:
                print(" × ", end="")
            print("%d" % i, end="")
            number //= i
            break
print("\n", end="")