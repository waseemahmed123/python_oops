class Test:
    x=100
    def __init__(self):
        self.a=10
        self.b=20
    def display(self):#when the method runs then only instance variable will be displayed otherwise constructor
        self.c=30
        
t=Test()
t.a=55
t.display()
t.d=40
print(t.__dict__)
print(Test.__dict__)#only produce when static variable are given