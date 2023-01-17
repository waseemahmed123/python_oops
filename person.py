class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatanddrink(self):
        print("Biryani Eating & Coke Drinking")
        
class SE(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print("Python Coding is something like.....")

class Student(Person):
class Teacher(Person):

        
s=SE("Waseem",32,100,10000)
print(s.name,s.age,s.eno,s.esal)
s.eatanddrink()
s.work()