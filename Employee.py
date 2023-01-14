class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print("Employee Number:",self.eno)
        print("EMployee Name:",self.ename)
        print("Employee Salary:",self.esal)
class Test:
    def modify(emp):
        emp.esal=emp.esal+1000
        emp.display()
e=Employee(100,"Durga",10000)
Test.modify(e)
