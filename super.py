class X:
    a=10
    def m1(self):
        print("Parent class instance method")
    @classmethod
    def m2(self):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent class static method")
    def __init__(self):
        self.b=8888
        print("parent Constructor")
class Y(X):   #first priority is child class if not child class than parent class will be reffered
    def __init__(self):
        super().m1()
        super().m2()
        super().m2()
        super().__init__()
        print(super().a)
        print(Y.a)
        print("Child constructor")
        
    

y=Y()