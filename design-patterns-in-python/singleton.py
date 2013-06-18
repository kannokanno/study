class Hoge:
    __instance__ = None

    def get_instance():
        if Hoge.__instance__ is None:
            Hoge.__instance__ = Hoge()
        return Hoge.__instance__

    get_instance = staticmethod(get_instance)


if __name__ == '__main__':
    a = Hoge.get_instance()
    b = Hoge.get_instance()
    print a
    print b
    print a == b
    print a is b
