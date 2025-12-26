#Implement polymorphism: Create two classes Rectangle and Circle with a method area() and calculate area differently for each.
class rectangle():
    def __init__(self,l ,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
class circle ():
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def area(self):
        return self.pi*(self.r*self.r)
obj1 =rectangle(5,6)
obj2= circle(3.14,5)
print(obj1.area())
print(obj2.area())

