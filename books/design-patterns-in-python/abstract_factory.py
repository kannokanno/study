# @see: http://weblog.nabetama.com/post/38624014910/python-abstractfactory


class Duck():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print 'Duck %s eating!!' % self.name


class Frog():
    def __init__(self, name):
        self.name = name

    def eat(self):
        print 'Frog %s eating!!' % self.name


class Algae():
    def __init__(self, name):
        self.name = name

    def grow(self):
        print 'Alage %s growing!!' % self.name


class WaterLily():
    def __init__(self, name):
        self.name = name

    def grow(self):
        print 'WaterLily %s growing!!' % self.name


class FrogAndAlgaeFactory():
    def new_animal(self, name):
        return Frog(name)

    def new_plant(self, name):
        return Algae(name)


class DuckAndWaterLilyFactory():
    def new_animal(self, name):
        return Duck(name)

    def new_plant(self, name):
        return WaterLily(name)


class Pond():
    def __init__(self, number_animals, number_plants, organism_factory):
        self.animals = []

        for i in range(1, number_animals + 1):
            param = "animal " + str(i)
            self.animal = organism_factory.new_animal(param)
            self.animals.append(self.animal)

        self.plants = []

        for i in range(1, number_plants + 1):
            param = "plant " + str(i)
            self.plant = organism_factory.new_plant(param)
            self.plants.append(self.plant)

    def simulate_now(self):
        [animal.eat() for animal in self.animals]
        [plant.grow() for plant in self.plants]


if __name__ == '__main__':
    pond = Pond(1, 4, FrogAndAlgaeFactory())
    pond.simulate_now()

    print "==="

    pond = Pond(2, 3, DuckAndWaterLilyFactory())
    pond.simulate_now()
