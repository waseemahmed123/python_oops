"""class Test:
    a=10
    def __init__(self):
        self.b=20
t2=Test()
t2.a+=1
print(t2.a)
print(Test.a)
"""
class Test1:
    a=10
    def __init__(self):
        Test1.b=20
    def m1(self):
        Test1.c=30
    @classmethod    
    def m2(cls):
        cls.d=40 #static variable value wont be modify a new instance value will be created for that object.
        Test1.e=50
    @staticmethod
    def m3():
        Test1.f=60
t=Test1()
t.m1()
t.m2()
t.m3()
Test1.g=70
print(Test1.__dict__)
    
                

        