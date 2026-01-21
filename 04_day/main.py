class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species
    def make_sound (self):
        print("make sound by lion roar")
class dog(animal):
    def __init__(self, name, species,breed):
        super().__init__(name, species)
        self.breed = breed 
    def show_dog(self):
        print(f"{self.name}\n{self.species}\n{self.breed}")
class cat(animal):
    def __init__(self,name,species,owner):
        super().__init__(name,species)
        self.owner = owner
    def shoe_cat(self):
        print(f"{self.name}\n{self.species}\n{self.owner}")

a = animal('lion','mufasa')
d = dog('kalu','bula','labrotor')
c = cat('pinky','cute','micky')
c.shoe_cat()
a.make_sound( )
