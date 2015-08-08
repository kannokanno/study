# -*- coding: utf-8 -*-
class MyClass:
    def f(self):
        print 11

obj = MyClass()
print obj
obj.f()

f_obj = obj.f
print f_obj
f_obj()


f_obj2 = obj.f
print f_obj2
print f_obj == f_obj2

class MyClass2:
    def __init__(self):
        # メソッド名と同名の場合、フィールド定義の方で上書きされる
        self.f = 'hoge'

    def f(self):
        print 11

obj = MyClass2()
print obj.f
# TypeError: 'str' object is not callable
# obj.f()


class MyClass3:
    def __init__(self, log):
        self.log = log

    def f(self, arg):
        self.log(arg)
        print arg

def logger_1(arg):
    print 'logging-1:', arg

def logger_2(arg):
    print 'logging-2:', arg

MyClass3(logger_1).f(11)
MyClass3(logger_2).f(22)

print MyClass
print MyClass2
print MyClass3
