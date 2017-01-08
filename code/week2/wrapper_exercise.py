class Struct:
    def __init__(self, some_list=None):
        if some_list is not None:
            self.my_list = some_list
        else:
            self.my_list = list()

    def insert(self, item):
        pass

    def delete(self, item):
        pass

    def max(self):
        pass

    def min(self):
        pass

    def inspect(self, printall=False):
        print("{} items in the list".format(len(self.my_list)))s
        if printall:
            print("The itmes are: ")
            for item in self.my_list:
                print("\t{}".format(item))


def test_struct():
    s0 = Struct()
    s0.insert(5)
    s0.insert(10)
    s0.insert(100)
    assert s0.max() == 100
    s0.delete(20)
    s0.delete(100)
    s0.delete(10)
    assert s0.max() == 5
    s0.inspect()


    x = [3,2,1]
    s1 = Struct(s1)
    s1.insert(23)
    assert s1.min() == 1
    s1.delete(1)
    assert s1.min() == 2
    s1.inspect()

if __name__ == "__main__":
    test_struct()
