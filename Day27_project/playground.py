def add(*args):
    sum=0
    for n in args:
        sum+=n
    return sum
#print(add(5,6,7,8,9,10))

#keyword arguments
def calculate(n,**kwargs):
    #print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]

    #print(n)
calculate(2,add=7,multiply=8)

#create a class with lots of optional kwargs

class Car:
    def __int__(self,**kwargs):
        self.make= kwargs["make"]
        self.model = kwargs.get("model")
my_car = Car(make="Nissan")
print(my_car.make)