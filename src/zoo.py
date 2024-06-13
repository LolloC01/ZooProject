class Animal:

    def __init__(self, name, species, age, width, height, preferred_habitat) -> None:
        """inizializzazione classe animal

        Args:
            name (str): nome dell'animale
            species (str): specie dell'animale
            age (int): età dell'animale
            width (float): larghezza dell'animale
            height (float): altezza dell'animale
            habitat (str): habitat dell'animale
            fence (Fence): indica il recinto in cui si trova l'animale
        """
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.height: float = height
        self.width: float = width
        self.preferred_habitat: str = preferred_habitat
        self.fence = None
        self.health: float = round(100 * (1 / age))

    def area_a(self, feed = False) -> float:
        """Calcola le dimensioni dell'animale

        Args:
            feed (bool, optional): Se True calcola la dimensione dell'animale dopo aver mangiato (incrementa del 2% altezza e larghezza). Defaults to False.

        Returns:
            float: ritorna le dimensioni dell'animale
        """
        if feed:
            x: float = (self.height+self.height*0.02)*(self.width+self.width*0.02)        # (self.height*0.02) * (self.width*0.02)   
            #y: float = self.height * self.width
            #x: float = y - x
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
        area: float = 0
        for x in self.animals:
            area += x.area_a()
        return self.area - area

class ZooKeeper:

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

    def add_animal(self, animal: Animal, fence: Fence) -> None:
        """Aggiunge un animale al recinto

        Args:
            animal (Animal): animale da aggiungere
            fence (Fence): recinto in cui aggiungere l'animale

        Returns:
            None
        """
        if animal.area_a() > fence.free_area():
            #print("NOT ENOUGHT SPACE IN THIS FENCE")   #gestire eccezione
            return 0
        else:
            if animal.preferred_habitat == fence.habitat:
                fence.animals.append(animal)
                animal.fence = fence
                #print("Animale aggiunto")
            else:
                pass#print("Habitat non compatibile con l'animale")

    def remove_animal(self, animal: Animal, fence: Fence) -> None:
        """rimuove l'animale dal recinto

        Args:
            animal (Animal): animale da rimuovere
            fence (Fence): recinto da cui rimuovere l'animale
        """
        if animal in fence.animals:
            fence.animals.remove(animal)
            animal.fence = None
        else:
            pass
            #print("ANIMAL NOT IN THIS FENCE")

    def feed(self, animal: Animal) -> None:
        """metodo per nutrire l'animale

        Args:
            animal (Animal): animale da nutrire
            fence (Fence): recinto i cui trovare l'animale

        Returns:
            None
        """
        #if animal.fence.free_area() >= animal.area_a(feed=True):
        x: float = animal.width * 0.02
        y: float = animal.height * 0.02
        z: float = animal.health * 0.01
        animal.width = animal.width + x
        animal.height = animal.height + y
        animal.health = animal.health + z
        if animal.area_a() > animal.fence.free_area():
            print("NOT ENOUGHT SPACE TO FEED THE ANIMAL")
        #else:
            #pass

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
        self.zoo_keepers: list[ZooKeeper] = []

    def describe_zoo(self) -> None:
        """
        Visualizza tutto lo zoo stampando prima la lista dei guardiani e poi la lista dei recinti con ogni animale all'interno
        """
        #print(f"Name={self.name} address={self.address}\n")
        print("Guardians: \n")
        for x in self.zoo_keepers:
            print(f"ZooKeeper(name={x.name}, surname={x.surname}, id={x.id})\n")
        print("Fences: \n")
        for x in self.fences:
            print(f"Fence(area={x.area}, temperature={x.temperature}, habitat={x.habitat})\n")
            print("with animals:\n")
            for y in x.animals:
                print(f"Animal(name={y.name}, species={y.species}, age={y.age})\n")
            print("#" * 30)
            print("")