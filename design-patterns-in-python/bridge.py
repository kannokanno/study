# -*- coding: utf-8 -*-
# @see http://ja.wikipedia.org/wiki/Bridge_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3

class BadPattern:
    class Dishware():
        pass

    class Plate(Dishware):
        pass

    class WoodenPlate(Plate):
        pass

    class GlassPlate(Plate):
        pass

    class Bowl(Dishware):
        pass

    class WoodenBowl(Bowl):
        pass

    class GlassBowl(Bowl):
        pass

    # もしカップ(Cup)を追加したくなった場合、Cup、WoodenCup、GlassBowlの3つを実装する必要がある
    # Wooden、Glassの他に実装が出てきた場合に影響範囲が大きい

    class Cup(Dishware):
        pass

    class WoodenCup(Cup):
        pass

    class GlassCup(Cup):
        pass


# Bridge
class GoodPattern:
    class Dishware():
        def __init__(self, material):
            self.material = material

    class Plate(Dishware):
        pass

    class Bowl(Dishware):
        pass

    class Material():
        pass

    class Wooden(Material):
        pass

    class Glass(Material):
        pass

    # もしカップ(Cup)を追加したくなった場合、Cupを新たに実装するだけでよく、直感的
    # Wooden、Glassの他に実装が出てきた場合も影響範囲が局所的で済む

    class Cup(Dishware):
        pass

if __name__ == '__main__':
    pass
