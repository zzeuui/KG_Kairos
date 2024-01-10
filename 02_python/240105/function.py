def say():
    print("hello")

#say()

def sayhello(name, birthyear):
    print(name)
    print(2024-birthyear)

#sayhello("yj", 1997)

def get_sum(n1, n2):
    return n1+n2

def get_two(n1, n2):
    return n1, n2

def odd_even(n):
    if n%2==0:
        return 0
    else:
        return 1

#print(get_sum(1, 2))
#print(get_two(1, 2))
#print(odd_even(3))

def greet(name, msg="hello"):
    print(name, '!', msg)

def keyw(x, y, z):
    return x+y-z

#greet('yj')
#greet('yj', 'nothing')
#print(keyw(x=1, y=5, z=2))

def param1(*args):
    print(args)

#param1(1,2,3)
#param1(1,2,3,4,5)

def param2(**kargs):
    print(kargs)

#param2(a=1, b=2, c=3)

a=1
def func1():
    b=2
    print(a, b)

def func2():
    b=333
    print(a, b)

#func1()
#func2()
