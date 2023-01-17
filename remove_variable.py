class Test:
    college_name="waseem academy"  #for constant value static variable is created. Example College name will be same.
    def __init__(self):#for evry changing objects instance variable is created
        self.a=10
        self.b=20
        self.c=30#like name of stuent wwill vary from object to object
        self.d=40
t1=Test()
t2=Test()
del t1.c  #remove variables
del(t2.d)
print("t1:",t1.__dict__)
print("t2:",t2.__dict__)