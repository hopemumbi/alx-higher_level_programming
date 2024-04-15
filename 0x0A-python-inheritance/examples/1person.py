#!/usr/bin/python3
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False

class Employee(Person):
    # Here we return true
    def isEmployee(self):
        return True

emp = Person('Hope')
print(emp.getName(), emp.isEmployee())

emp = Employee('Shi')
print(emp.getName(), emp.isEmployee())
