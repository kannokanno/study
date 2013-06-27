class Handler:
    def resolve(self, num):
        if self._resolve(num):
            return self._done(num)
        elif self._next is not None:
            return self._next.resolve(num)
        return False

    def set_next(self, handler):
        self._next = handler

    def _resolve(self, num):
        return False

class NumHandler(Handler):
    def _resolve(self, num):
      return not isinstance(num, bool) and \
              isinstance(num, (int, long, float, complex))

    def _done(self, num):
        return str(num) + ' is Some Number'

class OddHandler(NumHandler):
    def _resolve(self, num):
        return num % 2 != 0

    def _done(self, num):
        return str(num) + ' is Odd Number'

class MultipleNumHandler(NumHandler):
    def __init__(self, base):
        self.__base = base

    def _resolve(self, num):
        return num % self.__base == 0

    def _done(self, num):
        return str(num) + ' is Multiples of ' + str(num)

if __name__ == '__main__':
    odd = OddHandler()
    odd.set_next(NumHandler())
    handler = MultipleNumHandler(3)
    handler.set_next(odd)

    print handler.resolve(1)
    print handler.resolve(2)
    print handler.resolve(3)
