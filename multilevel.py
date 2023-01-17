class GF:
    def m1(self):
        print("Land")
class F(GF):
    def m2(self):
        print("Cash")
class U(F):
    def m3(self):
        print("Enjoy")
c=U()
c.m1()
c.m2()
c.m3()