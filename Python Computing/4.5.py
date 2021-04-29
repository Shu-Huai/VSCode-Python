import re

sentence = input("Please input a sentence: ")
pattern = re.compile(r'\b[a-zA-Z]{3}\b')
resultList = pattern.findall(sentence)
print("All words in this paragraph are 3 letters long: ", end="")
for i in range(len(resultList)):
    print(resultList[i], end="")
    if i != len(resultList) - 1:
        print(", ", end="")
print(".\n", end="")