class Entry:
    def __init__(self, name):
        self.entries = []
        self.name = name

    def add(self, entry):
        # do nothing
        pass

    def accept(self, visitor):
        visitor.visit(self)

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

class PrintUpperCaseNameVisitor:
    def visit(self, element):
        print element.name.upper()
        for e in element.entries:
            e.accept(self)

if __name__ == '__main__':
    d1 = Directory('Directory A')
    d1.add(File('File A'))
    d1.add(File('File B'))
    d1.add(File('File C'))

    d2 = Directory('Directory B')
    d2.add(File('File A'))
    d2.add(d1)

    d2.accept(PrintNameVisitor())
    print "--------------"
    d2.accept(PrintUpperCaseNameVisitor())
