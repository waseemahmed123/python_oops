class Test:
    a=10
    def __init__(self):
        self.b=20
        Test.c=30
    def m1(self): #instance variable can be created insdie class method but can be called when we run the method 
        self.d=40
        Test.e=50
    @classmethod
    def m2(cls):
        cls.f=60   #refrence to current class object f is also static variable
        Test.g=70
    @staticmethod
    def m3():
        Test.h=80
t=Test()
t.m1()
t.m1()
Test.m2()
Test.m3()
Test.i=90  #static variable can be declared from outside of the class


print(Test.__dict__)
print(t.a,t.b,t.c,t.d,t.e,t.f,t.g,t.h)  #we can access with reference object

