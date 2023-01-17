import time
class Test:
    def __init__(self):
        print("Object Innitialization...")
    def __del__(self):
        print("Fulfilling last wish and performing clean up activities...")
"""
t1=Test()
t1=None
time.sleep(5)
print("End of Application")  # destructor executes after the end of the program
"""
#or
t1=Test()
del t1
time.sleep(5)
print("End")  
