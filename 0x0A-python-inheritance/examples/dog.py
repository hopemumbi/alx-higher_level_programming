#!/usr/bin/python3
class Dog:
    """ Describes a Dog """
    kind = 'canine' # class variable shared by all instances

    def __init__(self, name):
        """ Initialize every instance of the class Dog """
        self.name = name # instance variable unique to each instance
        self.tricks = []

    def add_trick(self, trick):
        """ Add the trick that the dog can do """
        self.tricks.append(trick)

d = Dog('Zoe')
e = Dog('Nora')
d.add_trick('Stand')
e.add_trick('Sit')
print(d.name, d.tricks, d.kind)
print(e.name, e.tricks, e.kind)
