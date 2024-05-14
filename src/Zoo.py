class Animal:

    def __init__(self, name, species, age, width, height, habitat) -> None:
        """inizializzazione classe animal

        Args:
            name (_type_): nome dell'animale
            species (_type_): specie dell'animale
            age (_type_): età dell'animale
            width (_type_): larghezza dell'animale
            height (_type_): altezza dell'animale
            habitat (_type_): habitat dell'animale
        """
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = habitat
        self.health: float = round(100 * (1 / age))

    def area_a(self, feed = False) -> float:
        """Calcola le dimensioni dell'animale

        Args:
            feed (bool, optional): Se True calcola la dimensione dell'animale dopo aver mangiato (incrementa del 2% altezza e larghezza). Defaults to False.

        Returns:
            float: ritorna le dimensioni dell'animale
        """
        if feed:
            x = (self.height*0.02) * (self.width*0.02)
            y = self.height * self.width
            x = y - x
            return x
        return self.height * self.width


class Fence:

    def __init__(self, temperature, area, habitat) -> None:
        """Inizializza classe Fence (recinto)

        Args:
            temperature (float): indica la temperatura del recinto
            area (float): indica l'area del recinto
            habitat (string): indica il tipo di habitat del recinto
        """
        self.area: float = area
        self.temperature: float = temperature
        self.habitat: str = habitat
        self.animals: list[Animal] = []

    def free_area(self) -> float:
        """calcola l'area libera nel recinto

        Returns:
            float: ritorna lo spazio libero nel recinto
        """
        area = 0
        for x in self.animals:
            area += x.area_a()
        return self.area - area

class Zookeeper:

    def __init__(self, name, surname, id) -> None:
        """Inizializza la classe zookeeper (guardiano)

        Args:
            name (string): indica il nome del guardiano
            surname (string): indica il cognome del guardiano
            id (int): indica l'ID del guardiano
        """
        self.name: str = name
        self.surname: str = surname
        self.id: int = id

    def add_animal(animal: Animal, fence: Fence) -> None:
        """Aggiunge un animale al recinto

        Args:
            animal (Animal): animale da aggiungere
            fence (Fence): recinto in cui aggiungere l'animale

        Returns:
            None
        """
        if animal.area_a() > fence.free_area():
            print("NOT ENOUGHT SPACE IN THIS FENCE")   #gestire eccezione
            return 0
        else:
            if animal.preferred_habitat == fence.habitat:
                fence.animals.append(animal)
                print("Animale aggiunto")
            else:
                print("Habitat non compatibile con l'animale")

    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        """rimuove l'animale dal recinto

        Args:
            animal (Animal): animale da rimuovere
            fence (Fence): recinto da cui rimuovere l'animale
        """
        if animal in fence.animals:
            fence.animals.remove(animal)
        else:
            print("ANIMAL NOT IN THIS FENCE")

    def feed(self, animal: Animal, fence: Fence) -> None:
        """metodo per nutrire l'animale

        Args:
            animal (Animal): animale da nutrire
            fence (Fence): recinto i cui trovare l'animale

        Returns:
            None
        """
        if fence.free_area() >= animal.area_a(feed=True):
            x = animal.width * 0.02
            y = animal.height * 0.02
            z = animal.health * 0.01
            animal.width += x
            animal.height += y
            animal.health += z
        else:
            print("NOT ENOUGHT SPACE TO FEED THE ANIMAL")

    def clean(self, fence: Fence) -> float:
        """metodo per pulire il recinto

        Args:
            fence (Fence): recinto da pulire

        Returns:
            float: tempo impiegato per pulire il recinto
        """
        if fence.free_area() == 0:

            return fence.area
        x = fence.area - fence.free_area()
        return x / fence.free_area()



class Zoo:

    def __init__(self, name: str, address: str) -> None:
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