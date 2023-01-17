class Human:
    def __init__(self):
        self.name="waseem"
        self.head=self.Head()
        self.brain=self.Brain()
    def display(self):
        print("hello",self.name)
    class Head:
        def talk(self):
            print("Talking....")
    class Brain:
        def think(self):
            print("Thinking.....")
            
h=Human()
h.brain.think()