a=10
class Student:
    cname="Waseem Python"#static variable
    def __init__(self,name,rollno) -> None:
        self.name=name
        self.rollno=rollno
    def m1(self):
        self.cname="Ruby Python"
        x=10 #local variable
s1=Student()
s2=Student()

print(s1.m1())

