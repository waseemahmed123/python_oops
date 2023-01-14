class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hi",self.name)
        print("Youtmarks are:",self.marks)
    def grade(self):
        if self.marks>60:
            print("Yoy got second grade")
        elif self.marks>=50:
            print("You got secong Grade")
        elif self.marks>=35:
            print("You got third grade")
        else:
            print("You are failed")
n=int(input("Enter Number of Studdents:"))
for i in range(n):
    name=input("Enter STudent name:")
    marks=int(input("enter student marks:"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()
print("Student Name:",self.name)