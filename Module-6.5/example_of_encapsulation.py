class Employee:
    def __init__(self, name, salary, department) -> None:
        self.name = name    # public attribute
        self.__salary = salary    # private attribute
        self._department = department  # protect attribute

    def Get_salary(self):
        return self.__salary
    
    def Increase_salary(self, amount):
        self.__salary += amount

    def display(self):
        print(f"Name : {self.name} Department : {self._department}")

class Person(Employee):
    def __init__(self, name, salary, department) -> None:
        super().__init__(name, salary, department)

    def show(self):
        print(f"{self.__salary}")




obj = Person('Arafat', 12000, 'Accounting')
# obj.display()

# ob = Person()
# print(ob.name, ob.display())
# print(ob.show())
obj.show()


        