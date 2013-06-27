import random

class GraphObserver:
    def update(self, num):
        print '*' * num

class LogObserver:
    def update(self, num):
        print 'Generated: ' + str(num)

class RandomNumSubject:
    def __init__(self):
        self.observers = []

    def generate(self):
        num = random.randint(1, 20)
        for o in self.observers:
            o.update(num)
        return num

    def add_observer(self, observer):
        self.observers.append(observer)

if __name__ == '__main__':
    r = RandomNumSubject()
    print r.generate()

    r.add_observer(GraphObserver())
    r.add_observer(LogObserver())
    print r.generate()
    print r.generate()
