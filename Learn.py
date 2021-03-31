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
try:
    print(x[10])
except IndexError:
    print("No x[10].")
try:
    print(x.index(10))
except ValueError:
    print("No 10 in x.")
print("2 number in x: ", x.count(2))
print("1 number in x: ", x.count(1))
print("3 in x: ", 3 in x)
print("2 not in x: ", 2 not in x)
del x
List0 = [3, 5, 7, 9, 11]
List1 = ['a', 'b', 'c']
print("3, 'a' in zip: ", (3, 'a') in zip(List0, List1))
for a, b in zip(List0, List1):
    print(a, b)
s1='programming'
s2='language'
print(s1.capitalize() + ' ' + s2.upper())
