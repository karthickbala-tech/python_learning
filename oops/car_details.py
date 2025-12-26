#Create a class Car with attributes brand, model, and a method to display car details.
class Car():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print(f"the car model is {self.model}and brand is {self.brand}")
obj=Car('toyoto','mb116')
obj.display()

