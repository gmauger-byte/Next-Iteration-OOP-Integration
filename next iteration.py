class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class CatPet(Pet): #derived class using inheritance
    def __init__(self, name, age, color):
        super().__init__(name, "cat", age)
        self.color = color
        print(f"{name} is a {age}-year-old {color} cat.")
    
    def speak(self): #override method (polymorphism)
        self.name = "Cheeto"
        print(f"{self.name} says MERR")

cat = CatPet("Cheeto", 5, "orange")
cat.speak()



    
    


    

