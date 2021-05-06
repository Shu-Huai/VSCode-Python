class Kangaroo(object):
    def __init__(self, contents=None):
        if (contents == None):
            contents = []
        self.pouchContents_ = contents

    def __str__(self):
        stringList = [object.__str__(self) + " with pouch contents:"]
        for content in self.pouchContents_:
            stringList.append("    " + object.__str__(content))
        return "\n".join(stringList)

    def PutInPouch(self, content):
        self.pouchContents_.append(content)


kangaroo = Kangaroo()
testKangaroo = Kangaroo()
kangaroo.PutInPouch("wallet")
kangaroo.PutInPouch("car keys")
kangaroo.PutInPouch(testKangaroo)
print(kangaroo)
print(testKangaroo)