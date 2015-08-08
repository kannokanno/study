# Flyweight
class HeavyObj:
    def __init__(self, name):
        self.name = name

# Flyweight Factory
class Factory:
    def __init__(self):
        self._instances = {}

    def create(self, name):
        if name not in self._instances:
            print "create: " + name
            obj = HeavyObj(name)
            self._instances[name] = obj
        return self._instances[name]

if __name__ == '__main__':
    f = Factory()
    f.create('Foo')
    f.create('Foo')
    f.create('Bar')
    f.create('Foo')
    f.create('Baz')
    f.create('Baz')
