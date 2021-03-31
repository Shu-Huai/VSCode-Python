numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = numbers[8:6:-1]
print(number)
print(1 in numbers)
length = len(numbers)
maxnumber = max(numbers)
minnumber = min(numbers)
del numbers[9]
print(numbers)
numbers.append(10)
print(numbers)
print(id(numbers))
numbers.append(11)
print(id(numbers))
numbers += [12]
print(id(numbers))
print(id(numbers[0]))
numbers[0] = -1
print(id(numbers[0]))
print(id(numbers))
import time

start = time.time()
time.sleep(1)
print(time.time() - start)
x = list("fuck")
print(x)
x = [[10086] * 2] * 3
print(x)
x[0][0] = 1
print(x)
x = [1, 2, 1, 2, 1, 1, 1]
for i in x[0:7:1]:
    print(i)
    if i == 1:
        x.remove(i)
        print(x)