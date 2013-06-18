class Abstract:
    def open(self):
        print 'open'

    def process(self):
        self.open()
        self._concreate_process()
        self.close()

    def close(self):
        print 'close'

    def _concreate_process(self):
        pass


class ConcreateFoo(Abstract):
    def _concreate_process(self):
        print 'Foo'


class ConcreateBar(Abstract):
    def _concreate_process(self):
        print 'Bar'


if __name__ == '__main__':
    foo = ConcreateFoo()
    foo.process()
    print ''
    bar = ConcreateBar()
    bar.process()
