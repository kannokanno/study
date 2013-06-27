class Facade:
    def call(self, num):
        a = ComputeClientA()
        b = ComputeClientB()
        c = ComputeClientC()
        return a.call(b.call(c.call(num)))

class ComputeClientA:
    def call(self, num):
        return num * 10

class ComputeClientB:
    def call(self, num):
        return num + 10

class ComputeClientC:
    def call(self, num):
        return num / 2

if __name__ == '__main__':
    print Facade().call(10)
