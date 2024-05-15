from src.Zoo import Animal, Fence, Zookeeper, Zoo

# Creiamo alcuni animali
lion: Animal = Animal("Leo", "Lion", 5, 2.5, 1.5, "savannah")
tiger = Animal("Tigger", "Tiger", 4, 2.2, 1.4, "jungle")
elephant = Animal("Dumbo", "Elephant", 10, 3.5, 2.5, "savannah")

# Creiamo un recinto
savannah_fence = Fence(25, 13, "savannah")
jungle_fence = Fence(30, 50, "jungle")

# Creiamo uno zookeeper
zookeeper = Zookeeper("John", "Doe", 123)

# Aggiungiamo animali al recinto
Zookeeper.add_animal(lion, savannah_fence)
Zookeeper.add_animal(tiger, savannah_fence)
Zookeeper.add_animal(elephant, savannah_fence)

# Descriviamo lo zoo
zoo = Zoo("My Zoo", "123 Main Street")
zoo.fences.append(savannah_fence)
zoo.fences.append(jungle_fence)
zoo.zoo_keepers.append(zookeeper)
print(zoo.zoo_keepers[0].clean(zoo.fences[0]))
zoo.describe_zoo()
zoo.zoo_keepers[0].remove_animal(zoo.fences[0].animals[0], zoo.fences[1])
zoo.zoo_keepers[0].remove_animal(zoo.fences[0].animals[0], zoo.fences[0])
zoo.describe_zoo()
