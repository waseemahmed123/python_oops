import time
class Test:
    def __init__(self):
        print("Object Innitialization...")
    def __del__(self):
        print("Fulfilling last wish and performing clean up activities...")

t1=Test()
t2=t1
t3=t2
del t1
time.sleep(10)
print("Object not yet destroyed after deleting t1")
del(t2)
time.sleep(10)
print("Object not yet destroyed after deleting t2")
print("Iam trying to delete t3 object")
del(t3)
 
