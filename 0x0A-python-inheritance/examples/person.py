#!/usr/bin/python3
"""Module to demonstarte inheritance"""
class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Check if person is an employee
    def Display(self):
        print(self.name, self.id)

class Emp(Person):
    def Print(self):
        print("Emp class called")

Emp_details = Emp('Shi', 102)
Emp_details.Display()
Emp_details.Print()

emp = Person('Hope', 102)
emp.Display()
