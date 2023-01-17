class Student:
    """This is student class with required data"""
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("Student Name:{},RollNo:{},Marks:{}".format(self.name,self.rollno,self.marks))    
    
s1=Student("waseem",60,85)
s2=Student("ruby",62,89)
help(Student)


