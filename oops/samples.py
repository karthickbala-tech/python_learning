'''Create a class called Student that:

has two variables: name and age

has a method display() that prints name and age

👉 Your task: Write the code and create one object'''

class student():
    name="bala"
    age=25
    def display(self):
        print(self.name,self.age)
onj=student()
onj.display()

'''Question 8: Same Method, Different Behavior

Create:

class Dog → method sound()

class Cat → method sound()

👉 Task: Call both using a loop.'''
class dog():
    sound="brak"
    def display(self):
        print(self.sound)
class cat():
    sound="meeaww"
    def display(self):
        print(self.sound)
obj1=dog()
obj2=cat()
for i in (obj1,obj2):
    i.display()

