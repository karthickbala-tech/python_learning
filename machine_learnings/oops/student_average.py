#Create a class Student that stores marks in 3 subjects and has a method to calculate average marks.
class Student:
    def __init__(self,physics,math,chemistry):
        self.physics=physics
        self.math=math
        self.chemistry=chemistry
    def average(self):
        avg=float((self.physics+self.math+self.chemistry)//3)
        print(f"your average marks is {avg}")
obj1=Student(70,56,89)
obj1.average()

        