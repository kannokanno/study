class Entry:
    def __init__(self, name, size):
        self.entries = []
        self.name = name
        self.size = size

    def add(self, entry):
        # do nothing
        pass

    def accept(self, visitor):
        return visitor.visit(self)

class Directory(Entry):
    def add(self, entry):
        self.entries.append(entry)

class File(Entry):
    pass

class PrintNameVisitor:
    def visit(self, element):
        print element.name
        for e in element.entries:
            e.accept(self)

class CalcTotalSizeVisitor:
    def visit(self, element):
        total = element.size
        for e in element.entries:
            total += e.accept(self)
        return total

if __name__ == '__main__':
    d1 = Directory('Directory A', 1000)
    d1.add(File('File A', 200))
    d1.add(File('File B', 300))
    d1.add(File('File C', 500))

    d2 = Directory('Directory B', 2000)
    d2.add(File('File A', 2000))
    d2.add(d1)

    d2.accept(PrintNameVisitor())
    print "--------------"
    print "SIZE:" + str(d2.accept(CalcTotalSizeVisitor()))
