
class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return (self.name)
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return (self.marks)
n=int(input("Enter the number:")) 
for i in range(n):
    s=Student()
    name=input("Enter Name:")
    s.setName(name)
    marks=int(input("marks:"))
    s.setMarks(marks)
    print("hi",s.getName())
    print("Your marks are:",s.getMarks())
     
