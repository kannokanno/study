class Entry:
    def __init__(self, name):
        self.name = name

    def add(self, entry):
        # do nothing
        pass

class Directory(Entry):
    def __init__(self, name):
        Entry.__init__(self, name)
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def accept(self, visitor):
        return visitor.visit_dir(self)

class File(Entry):
    def __init__(self, name, size):
        Entry.__init__(self, name)
        self.size = size

    def accept(self, visitor):
        return visitor.visit_file(self)

class BadNamePrinter:
    def visit(self, element):
        print element.name
        if hasattr(element, 'entries'):
            for e in element.entries:
                self.visit(e)

class NamePrinter:
    def visit_file(self, element):
        print element.name

    def visit_dir(self, element):
        print element.name
        for e in element.entries:
            e.accept(self)

class SizeCalculator:
    def visit_file(self, element):
        return element.size

    def visit_dir(self, element):
        total = 0
        for e in element.entries:
            total += e.accept(self)
        return total

if __name__ == '__main__':
    d1 = Directory('Directory A')
    d1.add(File('File A', 200))
    d1.add(File('File B', 300))
    d1.add(File('File C', 500))

    d2 = Directory('Directory B')
    d2.add(File('File A', 2000))
    d1.add(d2)

    d1.accept(NamePrinter())
    BadNamePrinter().visit(d1)
    print "--------------"
    print "SIZE:" + str(d1.accept(SizeCalculator()))
