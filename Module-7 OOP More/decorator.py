import math
def outer(func):
    def inner(n):
        print("inner function start")
        func(n)
        print("inner function end")
    return inner


# outer()()
@outer
def get_factorial(n):
    # print("factorial value")
    fact = math.factorial(n)
    print("factorial of ", n," is : ", fact)


# outer(get_factorial)(11)
# get_factorial(5)

# outer(get_factorial)(11)

get_factorial(6)