def IsPrime(number):
    for i in range(2, number):
        if not number % i:
            return False
    return True


number = int(input("Please input a number: "))
print("%d is a prime: " % number, end="")
print(IsPrime(number))