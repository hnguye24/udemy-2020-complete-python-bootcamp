class Dog():
    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog("Lab", "Sammy", False)
my_dog2 = Dog(breed="Poodle", name="Phillis", spots=False)

print(my_dog.species)
print(my_dog2.species)