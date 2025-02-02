class stringWork:
    def __init__(self):
        self.word = ""
    def getString(self):
        self.word = input("write a word: ")
    def printString(self):
        print(self.word.upper())

s_1 = stringWork()
s_1.getString()
s_1.printString()