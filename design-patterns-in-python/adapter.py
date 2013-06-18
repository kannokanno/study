def show(target):
    target.show_foo()


class Adaptee:
    def __init__(self, name):
        self.name = name

    def show_bar(self):
        print 'show_bar:', self.name


class Adapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def show_foo(self):
        self.adaptee.show_bar()

if __name__ == '__main__':
    show(Adapter(Adaptee('Hello')))
