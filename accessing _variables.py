class Test:
    a=10
    def __init__(self):
        self.b=20
        
t1=Test()
t2=Test()
print("t1:",t1.a.t1.b)
print("t2:",t2.a.t2.b)
Test.a=888
t1.b=999 #change willl be applicable for t1 object not t2
print("t1:",t1.a.t1.b)
print("t2:",t2.a.t2.b)
