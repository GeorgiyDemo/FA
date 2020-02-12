from random import choice

class FordFocus():
    def __init__(self, color):

        self.color = color
    
    def get_field(self):
        return self.color


if __name__ == "__main__":

    colors = ["green", "black", "white","yellow"]
    for _ in range(10):

        obj = FordFocus(choice(colors))
        print(obj.get_field())