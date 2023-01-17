class Test:
    count=0
    y=0
    def __init__(self):
        Test.count+=1
    @classmethod
    def noOfobjects(cls,x):
        print("The number of objects created:",cls.count)
        cls.y=x
t1=Test()
t2=Test()

Test.noOfobjects(10)
print(Test.y)


