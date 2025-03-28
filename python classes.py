from python_classes2 import Cylinder
from python_classes3 import Account
from student import Student


class Person:
    def __init__(self, name, age): # constructor
        print("Creating a person")
        self.name = name
        self.age = age
    def say_hello(self):
        print(f"Hello, i am {self.name} and I am {self.age} years old")

p1 = Person("Jack", 19)
p2 = Person("Miry" ,  23)
p3 = Person("Zack", 80)

p1.say_hello()
p2.say_hello()
p3.say_hello()



# objects ==data + function
name = "Chan"
name.upper()

c1 = Cylinder(10, 32)
c2 = Cylinder(66.65, 890)

c1. volume()
c1.print_details()


acc1 = Account("0002", "Mary", 2000000)
acc2 = Account("0003", "John", 890000)

acc2.deposit(1000)
acc2.check_balance()
acc2.withdraw(200)
acc2.check_balance()


student1 = Student("23/3/2006","John","Male" )
print(f"student name: {student1.name} is {student1.calculate_age()}years old")