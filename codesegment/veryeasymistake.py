#encoding: utf-8

# website: http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make

'''
# Misunderstanding Python scope rules
x = 10
def foo():
    x += 1
    print x

foo()
'''

'''
# Modifying a list while iterating over it
odd = lambda x: bool(x % 2)
numbers = [n for n in range(10)]
for i in range(len(numbers)):
    if odd(numbers[i]):
        del numbers[i]
'''

'''
# Confusing how Python binds variables in closures
# error
def create_multipliers():
    return [lambda x : i * x for i in range(5)]
for mul in create_multipliers():
    print mul(2)

# ok
def create_multipliers():
    return [lambda x, i=i : i * x for i in range(5)]

for mul in create_multipliers():
    print multiplier(2)
'''





