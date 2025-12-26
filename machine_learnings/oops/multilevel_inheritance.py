class Animal:
    def sound(self):
        print("Animal makes a sound.")

class Pet:
    def sound(self):
        print("Pet sound.")

class Dog(Animal, Pet):  
    def sound(self):
        super().sound()
        Pet.sound(self)
        
        print("Dog barks.")

class Puppy(Dog):  
    def sound(self):
        super().sound()
        print("Puppy whines.")

puppy = Puppy()
puppy.sound()   
