import sys
class Test:
    pass
t1=Test()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))  #it will also count self
del(t1)
print(sys.getrefcount(t2))