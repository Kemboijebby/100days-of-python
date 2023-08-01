class Animal:
    def __init__(self):
        self.num_eyes=2

    def breath(self):
        print("Exhale,inhale")
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

nemo=Fish()
nemo.breath()
nemo.swim()
print(nemo.num_eyes)

