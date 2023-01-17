class Student:
    def __init__(self,n="",m=0):
        self.name=n
        self.marks=m
    def display(self):
        print("Hi",self.name)
        print("Marks:",self.marks)
s1=Student()
s1.display()

s2=Student("Waseem",100)
s2.display()