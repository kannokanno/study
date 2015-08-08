# RealSubject
class Database:
    def __init__(self, name):
        self.name = name
        self.connect()

    def connect(self):
        print "Real Connect..."

# Proxy
class DatabaseProxy:
    def __init__(self, name):
        self.name = name
        self.real = None

    def connect(self):
        if self.real is None:
            self.real = Database(self.name)

if __name__ == '__main__':
    real = Database('HogeDB')

    print '----------'

    proxy = DatabaseProxy('HogeDB')
    print proxy.name
    proxy.connect()
    print proxy.name
