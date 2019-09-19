import collections

class CheckClass(object):
    def __init__(self):
        self.custom_tuple()
        self.standart_dictionary()
    
    def custom_tuple(self):
        ctuple = collections.namedtuple("Koshkas","name value")
        custom = []
        custom.append(ctuple("Kot",1))
        print(ctuple)
        print(custom)
    
    def standart_dictionary(self):
        Koshkas = {
            "name" : [],
            "value": [],
        }
        Koshkas["name"] = "Kot"
        Koshkas["value"] = 1
        print(Koshkas)

if __name__ == "__main__":
    CheckClass()