class Father:
    def height(self):
        print("Height is 6 Feet")
class Mother:
    def color(self):
        print("Brown color")
        
class Child(Father,Mother):
    print("Child inherited properties from parents")
c=Child()
c.height()
c.color()
        
