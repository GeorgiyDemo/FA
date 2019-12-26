from collections import MutableSequence

class DEMKACollection(MutableSequence):
    """
    Кастомная коллекция
    """
    def __init__(self, data=None):
        """Initialize the class"""
        super(DEMKACollection, self).__init__()
        if (data is not None):
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __len__(self):
        """List length"""
        return len(self._list)

    def __getitem__(self, ii):
        """Get a list item"""
        return self._list[ii]

    def __delitem__(self, ii):
        """Delete an item"""
        del self._list[ii]

    def __setitem__(self, ii, val):
        # optional: self._acl_check(val)
        self._list[ii] = val

    def __str__(self):
        return str(self._list)

    def insert(self, ii, val):
        # optional: self._acl_check(val)
        self._list.insert(ii, val)

    def append(self, val):
        self.insert(len(self._list), val)

class MainClass():
    def __init__(self):
        self.my_collection = DEMKACollection([1,5,3,2,5])
        print(type(dem))
        for x in dem:
            print(x)

if __name__=='__main__':
    MainClass()
