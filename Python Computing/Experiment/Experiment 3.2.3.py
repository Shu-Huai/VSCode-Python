import os
import random
import re
import jieba
from tqdm import trange


class Markov():
    def __init__(self, n: int = 1, path: str = "", text_type="English"):
        self.path_ = path
        self.type_ = text_type
        self.n_ = n
        self.txt_ = self.GetPath()
        self.words_ = self.TextProcession()
        self.wordsDictionary_ = self.Analyze()

    def GetPath(self):
        path = os.path.join(os.getcwd(), self.path_ + ".txt")
        if os.path.exists(path):
            with open(path) as txt:
                return txt.read()
        else:
            return ""

    def TextProcession(self) -> list:
        path = os.path.join(os.getcwd(), self.path_ + "_segmentation.txt")
        if os.path.exists(path):
            with open(path) as file_obj:
                text = file_obj.read()
                words = text.split(" ")
            return words
        else:
            text = self.txt_.replace("\n", " ").replace("[", " ").replace("]", " ")
            r = "[-*#\"\"\\()%“‘’”、（）|=\d<>《》/]+"
            text = re.sub(r, "", text)
            if self.type_ == "English":
                for symbol in [",", ".", ":", ";", "?", "!"]:
                    text = re.sub("[{}]+".format(symbol), " " + symbol + " ", text)
                words = [word.lower() for word in text.split(" ") if not word.isspace()]
            else:
                words = [word.strip() for word in jieba.cut(text) if not word.isspace()]
            return words

    def SaveSegmentation(self):
        path = os.path.join(os.getcwd(), self.path_ + "_segmentation.txt")
        with open(path, "w") as file_obj:
            for word in self.words_:
                file_obj.write(word + " ")

    def Analyze(self) -> dict:
        wordsDictionary = {}
        count = len(self.words_) // self.n_ if self.n_ != 1 else len(self.words_) // self.n_ - 1
        print("Start analyzing")
        for i in trange(count):
            word = tuple([self.words_[i + j] for j in range(self.n_)])
            if word not in wordsDictionary:
                wordsDictionary[word] = {}
            wordsDictionary[word][self.words_[i + self.n_]] = wordsDictionary[word].get(self.words_[i + self.n_], 0) + 1
        return wordsDictionary

    def SaveDictionary(self):
        with open(self.path_ + "_dict_{}.txt".format(str(self.n_)), "w") as file:
            for key, value in self.wordsDictionary_.items():
                for word in key:
                    file.write(word + " ")
                file.write("\n")
                for _key, _value in value.items():
                    file.write("\t\t" + _key + ": " + str(_value) + "\n")

    def WordFrequencySum(self, fre_dict: dict) -> int:
        sum = 0
        for word, value in fre_dict.items():
            sum += value
        return sum

    def FetchSuffix(self, dictionary: dict) -> str:
        temp = random.randint(1, self.WordFrequencySum(dictionary))
        for word, value in dictionary.items():
            temp -= value
            if temp <= 0:
                return word

    def Generate(self, length: int = 100, words: str = ""):
        chain = ""
        if not words:
            words = random.choice(list(self.wordsDictionary_.keys()))
        else:
            for wordsTuple in self.wordsDictionary_.keys():
                if words == wordsTuple[0]:
                    words = wordsTuple
            if not isinstance(words, tuple):
                words = random.choice(list(self.wordsDictionary_.keys()))
        print("Start generating")
        for i in trange(length):
            for word in words:
                chain += word
                if self.type_ == "English":
                    chain += " "
            words = self.FetchSuffix(self.wordsDictionary_[words])
            key = []
            for wordsTuple in self.wordsDictionary_.keys():
                if words == wordsTuple[0]:
                    key.append(wordsTuple)
            words = random.choice(key)
        return chain


markov = Markov(2, r"Python Computing\Experiment\whitefang")
markov.SaveSegmentation()
print("The chain is: %s" % markov.Generate(20))