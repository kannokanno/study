from collections import namedtuple

Book = namedtuple('Book', 'name')


class BookShelf:
    def __init__(self):
        self.books = []

    def size(self):
        return len(self.books)

    def get(self, index):
        return self.books[index]

    def append(self, book):
        self.books.append(book)

    def iterator(self):
        return Iterator(self)


class Iterator:
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.size = aggregate.size()
        self.index = 0

    def has_next(self):
        return self.index < self.size

    def next(self):
        obj = self.aggregate.get(self.index)
        self.index += 1
        return obj

if __name__ == '__main__':
    shelf = BookShelf()
    shelf.append(Book('first'))
    shelf.append(Book('second'))
    shelf.append(Book('third'))

    it = shelf.iterator()
    print it.has_next()
    print it.next().name
    print it.has_next()
    print it.next().name
    print it.has_next()
    print it.next().name
    print it.has_next()  # => False
    print it.next().name  # => index out of range
