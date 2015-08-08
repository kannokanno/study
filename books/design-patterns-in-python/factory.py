class Factory:
    def create(self, name):
        print 'before create'
        p = self._create_product(name)
        print ' after create'
        return p

    def _create_product(self, name):
        pass


class UpperFactory(Factory):
    def _create_product(self, name):
        return Product(name.upper())


class LowerFactory(Factory):
    def _create_product(self, name):
        return Product(name.lower())


class Product:
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    print UpperFactory().create('Bob').name
    print LowerFactory().create('Bob').name
