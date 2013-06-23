class Entry:
    def __init__(self, name):
        self.name = name

    def add(self, entry):
        # do nothing
        pass

    def show(self):
        print self.name

class Directory(Entry):
    def __init__(self, name):
        self.entries = []
        Entry.__init__(self, name)

    def add(self, entry):
        self.entries.append(entry)

    def show(self):
        print self.name
        for e in self.entries:
            e.show()

class File(Entry):
    def __init__(self, name):
        Entry.__init__(self, name)


if __name__ == '__main__':
    d1 = Directory('Directory A')
    d1.add(File('File A'))
    d1.add(File('File B'))
    d1.add(File('File C'))

    d2 = Directory('Directory B')
    d2.add(File('File A'))
    d2.add(d1)

    d2.show()
