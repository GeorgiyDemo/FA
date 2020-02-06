class CleckClass():
    def __init__(self, field):
        self.field = field
    
    def get_field(self):
        return self.field


if __name__ == "__main__":
    obj = CleckClass("meow")
    print(obj.get_field())