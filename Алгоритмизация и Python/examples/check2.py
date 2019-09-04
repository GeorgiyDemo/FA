class CheckerClass():
    def __init__(self, str):
        self.meow_str =  str
        self.check()
    
    def check(self):
        print(self.meow_str)


if __name__ == "__main__":
    obj = CheckerClass("meow")
    strs = obj.meow_str
    print(strs.swapcase())

