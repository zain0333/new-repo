# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds.")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks.")

# Create object
d = Dog()

# Call methods
d.sound()   # Inherited from Animal
d.bark()    # Method of Dog