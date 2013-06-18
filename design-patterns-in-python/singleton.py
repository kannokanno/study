from copy import deepcopy


class Manager:
    def __init__(self):
        self._prototypes = {}

    def register(self, key, prototype):
        self._prototypes[key] = prototype

    def create(self, key):

        return deepcopy(self._prototypes[key])


class Marker:
    def __init__(self, mark):
        self.mark = mark

    def use(self, str):
        return self.mark + str + self.mark

if __name__ == '__main__':
    manager = Manager()
    manager.register('marker', Marker('*'))

    strong = manager.create('marker')
    print strong.use('Hello')

    delete = manager.create('marker')
    delete.mark = '-'
    print delete.use('Hello')
