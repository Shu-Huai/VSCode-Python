def DoTwice(function0):
    function0()
    function0()


def DoFour(function0):
    DoTwice(function0)
    DoTwice(function0)


def PrintBeam():
    print("+ - - - -"),


def PrintPost():
    print("|        "),


def PrintBeams():
    DoTwice(PrintBeam)
    print("+")


def PrintPosts():
    DoTwice(PrintPost)
    print("|")


def PrintRow():
    PrintBeams()
    DoFour(PrintPosts)


def PrintGrid():
    DoTwice(PrintRow)
    PrintBeams()


PrintGrid()


def OneFourOne(function0, function1, function2):
    function0()
    DoFour(function1)
    function2()


def PrintPlus():
    print("+"),


def PrintDash():
    print("-"),


def PrintBar():
    print("|"),


def PrintSpace():
    print(" "),


def PrintEnd():
    print


def Nothing():
    print("", end="")


def PrintOneBeam():
    OneFourOne(Nothing, PrintDash, PrintPlus)


def PrintOnePost():
    OneFourOne(Nothing, PrintSpace, PrintBar)


def PrintFourBeams():
    OneFourOne(PrintPlus, PrintOneBeam, PrintEnd)


def PrintFourPosts():
    OneFourOne(PrintBar, PrintOnePost, PrintEnd)


def PrintRow():
    OneFourOne(Nothing, PrintFourPosts, PrintFourBeams)


def PrintGrid():
    OneFourOne(PrintFourBeams, PrintRow, Nothing)


PrintGrid()
comment = """
After writing a draft of the 4x4 grid, I noticed that many of the
functions had the same structure: they would do something, do
something else four times, and then do something else once.

So I wrote one_four_one, which takes three functions as arguments; it
calls the first one once, then uses do_four to call the second one
four times, then calls the third.

Then I rewrote print1beam, print1post, print4beams, print4posts,
print_row and print_grid using one_four_one.

Programming is an exploratory process.  Writing a draft of a program
often gives you insight into the problem, which might lead you to
rewrite the code to reflect the structure of the solution.

--- Allen
"""
print(comment)