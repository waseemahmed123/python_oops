class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
n=int(input("Enter Number of Students:"))
for i in range(n):
    s=Student()
    name=input("Enter name of student:")
    s.setName(name)
    marks=int(input("Enter Marks of Students:"))
    s.setMarks(marks)