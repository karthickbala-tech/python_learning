#Implement inheritance: a base class Animal with method sound() and derived classes Dog and Cat overriding sound().
class animal():
    def sound(self):
        print("Animal makes a sound")
class dog(animal):
    pass
    '''def sound(self):
        super().sound()
        print("bark")'''
        
class cat(animal):
    def sound(self):
        print('meaawwww')
obj1=dog()
obj2=cat()
obj1.sound()
obj2.sound()
