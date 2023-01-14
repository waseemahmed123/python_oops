class Duck:
    def talk():
        print("quack,quack")
class Dog:
    def talk(self):
        print("Bow Bow")
class Cat:
    def talk(self):
        print("Meow,Meow")
class Goat:
    def talk(self):
        print("myah,myah")
l=[Duck(),Dog(),Goat(),Cat()]
for obj in l:
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
    
        