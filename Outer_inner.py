class Outer:
        
    def m1(self):
        print("Outer class Method")
    class Inner:
        def m2(self):
            print("Inner class Method")
Outer().Inner().m2()
