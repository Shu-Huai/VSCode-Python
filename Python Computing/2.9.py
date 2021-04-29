dictation = {1: "a", 2: "b", 3: "c", 4: "d"}
inputKey = int(input("Please input a key: "))
value = dictation.get(inputKey, "The key you entered does not exist!")
if value != "The key you entered does not exist!":
    print("The value is: ", end="")
print(value)