class Person:

    def __init__(self, name):
        self.name = name


class Joe(Person):

    def __init__(self, name):
        Person.__init__(self, name)

    def hi(self):
        print "Hi, my name is ", self.name
