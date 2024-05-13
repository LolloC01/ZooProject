class Animal:

    def __init__(self, name, species, age, width, height, habitat) -> None:
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = habitat
        self.health: float = round(100 * (1 / age))

    def area_a(self, feed = False) -> float:
        if feed:
            x = (self.height*0.02) * (self.width*0.02)
            x -= self.height * self.width
            return x
        return self.height * self.width


class Fence:

    def __init__(self, temperature, area, habitat) -> None:
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []

    def free_area(self) -> float:
        area = 0
        for x in self.animals:
            area += x.area_a()
        return self.area - area

class Zookeeper:

    def __init__(self, name, surname, id) -> None:
        self.name: str = name
        self.surname: str = surname
        self.id: int = id

    def add_animal(animal: Animal, fence: Fence) -> None:
        if animal.area_a() > fence.free_area():
            print("NOT ENOUGHT SPACE IN THIS FENCE")   #gestire eccezione
            return 0
        else:
            if animal.preferred_habitat == fence.habitat:
                fence.animal.append(animal)
                print("Animale aggiunto")
            else:
                print("Habitat non compatibile con l'animale")

    def remove_animal(animal: Animal, fence: Fence) -> None:
        if animal in fence:
            del fence.animals[animal]
        else:
            print("ANIMAL NOT IN THIS FENCE")

    def feed(animal: Animal, fence: Fence) -> None:
        if fence.free_area() >= animal.area_a(feed=True):
            animal.width *= 0.02
            animal.height *= 0.02
            animal.health *= 0.01

    def clean(fence: Fence) -> float:
        if fence.free_area() == 0:
            return fence.area
        x = fence.area - fence.free_area()
        return x / fence.free_area()



class Zoo:
    
    def __inti__(self, name: str, address: str) -> None:
        """inizializzo lo zoo

        Args:
            name (str): Nome dello zoo
            address (str): Indirizzo dello zoo
        """
        self.name: str = name
        self.address: str = address
        self.fences: list[Fence] = []
        self.zoo_keepers: list[Zookeeper] = []

    def describe_zoo(self) -> None:
        """
        Visualizza tutto lo zoo stampando prima la lista dei guardiani e poi la lista dei recinti con ogni animale all'interno
        """
        print("Guardians: \n")
        for x in self.zoo_keepers:
            print(f"Name: {x.name}\tSurname: {x.surname}\t ID: {x.id}")
        print("\n Fences \n")
        for x in self.fences:
            print(f"Fence: \n\thabitat: {x.habitat}\n\ttemperature: {x.temperature}\n\tarea: {x.area}\n with this animals:")
            for y in x.animals:
                print(f"{y.name}\t{y.species}\t{y.age}")
            print("#" * 30)



lion = Animal("lion", "felino", 7, 3.45, 1.38, "savana")
