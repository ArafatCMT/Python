from menu import Menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = [] # eta ak ta database
        self.menu = Menu()

    def add_employees(self, employee):
        self.employees.append(employee)
        print(f"\n\t-->> {employee.name} is added successfully !!")

    def view_employees(self):
        print("\n\tEmployee List:")
        print("\n\tName\t\tEmail \t\tPhone\t\tAddress\t\tAge\t\tDesignation\tSalary")
        for emp in self.employees:
            print(f"\t{emp.name}\t\t{emp.email}\t{emp.phone}\t\t{emp.address}\t\t{emp.age}\t\t{emp.designation}\t\t{emp.salary}")