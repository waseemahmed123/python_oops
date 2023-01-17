class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("Employee Number:",self.eno)
        print("Employee name:",self.ename)
        print("Employee salary:",self.esal)
        print("Employee address:",self.eaddr)
        
e1=Employee(200,"waseem",200000,"Bhopal")
e2=Employee(300,"Ruby",300000,"Hyd")
e1.display()
e2.display()
