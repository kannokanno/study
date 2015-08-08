# -*- coding: utf-8 -*-

# 関数がファーストクラスなら、
# Commandの代わりに関数オブジェクトを扱えばいいんじゃないかという気もしている

# ConcreteCommand
class MoveLeft:
    def execute(self, point):
        point.move_left()

# ConcreteCommand
class MoveRight:
    def execute(self, point):
        point.move_right()

# ConcreteCommand
class MoveUp:
    def execute(self, point):
        point.move_up()

# ConcreteCommand
class MoveDown:
    def execute(self, point):
        point.move_down()

# Receiver
class Point:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def move_left(self):
        self.__x -= 1
        self.__move('Left')

    def move_right(self):
        self.__x += 1
        self.__move('Right')

    def move_up(self):
        self.__y += 1
        self.__move('Up')

    def move_down(self):
        self.__y -= 1
        self.__move('Down')

    def __move(self, direct):
        print 'Move ' + direct, (self.__x, self.__y)

# Invoker
class Invoker:
    def __init__(self):
        self.commands = []

    def execute(self, point):
        for c in self.commands:
            c.execute(point)

    def add_command(self, command):
        self.commands.append(command)

if __name__ == '__main__':
    invoker = Invoker()
    invoker.add_command(MoveLeft())
    invoker.add_command(MoveUp())
    invoker.add_command(MoveLeft())
    invoker.add_command(MoveDown())
    invoker.add_command(MoveRight())
    invoker.add_command(MoveRight())

    point = Point()
    invoker.execute(point)
