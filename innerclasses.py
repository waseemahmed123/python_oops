class Outer:
    def m1(self):
        print("Outer class Method")
        
    class Inner:    #Nested classes
        def m2(self):
            print("Inner class Method")
o=Outer()
o.m1()
i=o.Inner()
i.m2()
#Outer().Inner().m2()
