class Person:
    def __init(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print("Biryani eating and coke drinking")
    
class SE(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(self,name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print("Pythin Coding is too difficult")
        
s=SE("Waseem",48,100,10000)
print(s.name,s.age)
