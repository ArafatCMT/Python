class Singleton:
    __instance = None
    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception("Already have an instance, use that one by calling get instance method")
        
    @staticmethod
    def Get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    

first = Singleton.Get_instance()
second = Singleton.Get_instance()
print(first)
print(second)

last = Singleton()