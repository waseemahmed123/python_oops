class Person:
    def __init__(self):
        print("Person Class Constrructor")
        self.name="Waseem"
        self.db=self.Dob()
    def display(self):
        print("Name:",self.name)
    class Dob:
        def __init__(self):
            print("Dob class Constructor")
            self.dd=28
            self.mm=5
            self.yy=1947
        def display(self):
            print("Dob={}/{}/{}".format(self.dd,self.mm,self.yy))
p=Person()
p.display()
p.db.display()

