import os

# case1
try:
    print open(os.path.dirname(__file__) + '/fib.py', 'r').readline()
except EnvironmentError as err:
    sys.exit(1)

# case2
with open(os.path.dirname(__file__) + '/fib.py', 'r') as fp:
    print fp.readline()
