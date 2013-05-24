try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print type(inst)
    print inst.args
    print inst
    x, y = inst
    print 'x = ', x
    print 'y = ', y

try:
    raise Exception()
except Exception as inst:
    print type(inst)
    print inst.args
    print inst

try:
    print 1
except:
    print 2
else:
    print 3
finally:
    print 4
