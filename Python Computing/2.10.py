from random import randint

originList = [randint(0, 100) for i in range(20)]
tempList = originList[0:10]
tempList.sort()
originList[0:10] = tempList
tempList = originList[10:20]
tempList.sort(reverse=1)
originList[10:20] = tempList
print("The list is: ")
print(originList)