# inheritance

class Employee:
    def __init__(self, name, id, salary, department) -> None:
        self.name = name
        self.id = id
        self.__salary = salary # Access Modifire : private 
        self.department = department

    def get_data(self):
        return f'Name : {self.name} and Department : {self.department}'
    
    def get_salary(self):
        return self.__salary
    

class Person(Employee):
    def __init__(self, name, id, salary, department) -> None:
        super().__init__(name, id, salary, department)
        


afjal = Person('Afnan', 101, 15000, 'IT_Programming')

print(afjal.get_data())
# print(afjal.salary)
print(afjal.get_salary())