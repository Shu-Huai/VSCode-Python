import re

sentence = input("Please input a sentence: ")
pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
matchResult = pattern.search(sentence)
sentence = pattern.sub(matchResult.group(1), sentence)
print("The sentence is: ", end="")
print(sentence)