class Singleton:
    __intance = None
    def __init__(self, name) -> None:
        if Singleton.__intance is None:
            Singleton.__intance = name
        else:
            raise Exception("Already have an instance")

    @staticmethod 
    @property
    def get_instance(name):
        if Singleton.__intance is None:
            Singleton(name)
        return Singleton.__intance
    

# first = Singleton.get_instance('arafat')
# print(first)
# second = Singleton.get_instance('rafat')
# print(second)

obj = Singleton('arafat')
print(Singleton.get_instance)