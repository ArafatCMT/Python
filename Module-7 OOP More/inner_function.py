def outer_function():
    print("Outer Function")
    def inner_function(value):
        print("Inner Function")
        return value
    return inner_function

# print(outer_function())
# print(outer_function()(1000))


def do_something(work):
    print("Start work")
    print(work())
    # work()
    print("End Work")

def coding():
    print("coding with python")
    return 500

do_something(coding)

