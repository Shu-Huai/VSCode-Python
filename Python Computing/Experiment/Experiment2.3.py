def compare(line, compareline):
    if len(line) != len(compareline):
        return 0
    for i in range(len(line)):
        if line[i] != compareline[len(line) - i - 1]:
            return 0
    return 1


file = open("D:\Visual Studio Code\Visual-Studio-Code-Python\Python Computing\Experiment\words.txt")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n', '')
reversedwords = []
for line in lines:
    for compareline in lines:
        if line != compareline and compare(line, compareline) and line not in reversedwords:
            reversedwords.append(line)
            reversedwords.append(compareline)
            print("(" + line + ", " + compareline + ")")