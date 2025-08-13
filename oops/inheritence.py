# single inheritence
class car:
    @staticmethod
    def start():
        print("car has started!")

    @staticmethod
    def stop():
        print("car has stoped!")

class toyotacar(car):

    def __init__(self,name):
        self.name =name

c1 =car("fortuner")
c2 =car("thar")

print(c1.name)
print(c1.start())

# multi-level inheritence

class cars:
    @staticmethod
    def start():
        print("car has started!")

    @staticmethod
    def stop():
        print("car has stoped!")

class maruti(cars):

    def __init__(self,brand):
        self.brand =brand

class swift_dzire(maruti):
    def __init__(self, type):
        self.type =type

car1 =maruti("deasel")
car1.start()

# multiple inheritence

class A:
    var1 ="this is class A"

class B:
    var2 ="this is class B"

class C(A,B):
    var3 ="this is class C"

c1= C()
print(c1.var3)
print(c1.var1)
print(c1.var2)
