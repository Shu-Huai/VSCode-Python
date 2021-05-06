import re

sentence = input("Please input a sentence: ")
pattern = re.compile(r'(?:[^\w]|\b)i(?:[^\w])')
while True:
    result = pattern.search(sentence)
    if result:
        if result.start(0):
            sentence = sentence[:result.start(0) + 1] + 'I' + sentence[result.end(0) - 1:]
        else:
            sentence = sentence[:result.start(0)] + 'I' + sentence[result.end(0) - 1:]
    else:
        break
print("The sentence is: ", end="")
print(sentence)