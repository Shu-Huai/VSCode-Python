from random import randint

numberList = [randint(-65535, 65536) for i in range(20)]
evenNumberList = numberList[::2]
evenNumberList.sort(reverse=1)
numberList[::2] = evenNumberList
print("The list is:")
print(numberList)