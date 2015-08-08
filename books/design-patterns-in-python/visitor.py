# -*- coding: utf-8 -*-
# なんだかモヤモヤしていたが、http://www.aerith.net/design/Visitor-j.htmlの解説を読むと
# 以下のコード例は適切ではないと思えてきた。けど一応残しておく
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

# BAD:状態を保持できない(状態変数を引き回すかグローバル変数にしないと)
class BadNamePrinter1:
    # indentは省略
    def visit(self, element):
        # BAD:もしDevice(Entry)クラスが新規追加された場合に対応できない
        #     (entriesメソッドの有無 = 型判別ではないので)
        if hasattr(element, 'entries'):
            print element.name
            for e in element.entries:
                self.visit(e)
        else:
            print element.name

class BadNamePrinter2:
    def __init__(self):
        self.indent = ''
        self.before = ''

    def visit(self, element):
        # BAD:新しいEntryクラスが出来ても対応はできるが、処理が膨れる
        if isinstance(element, File):
            if self.before is 'dir':
                self.indent += '  '
            print self.indent + element.name
            self.before = 'file'
        else:
            print self.indent + element.name
            self.before = 'dir'
            for e in element.entries:
                self.visit(e)

class NamePrinter:
    def __init__(self):
        self.indent = ''
        self.before = ''

    def visit_file(self, element):
        if self.before is 'dir':
            self.indent += '  '
        print self.indent + element.name
        self.before = 'file'

    def visit_dir(self, element):
        self.before = 'dir'
        print self.indent + element.name
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
    print "--------------"
    BadNamePrinter1().visit(d1)
    print "--------------"
    BadNamePrinter2().visit(d1)
    print "--------------"
    print "SIZE:" + str(d1.accept(SizeCalculator()))
