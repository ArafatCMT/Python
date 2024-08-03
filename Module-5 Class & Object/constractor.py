class Student:
    def __init__(self, Name, Roll, Department):
        self.Name = Name
        self.Roll = Roll
        self.Department = Department

n = int(input())
lst = []

for i in range(0,n):
    name, roll, department = map(str,input().split())
    # roll = int(roll)
    # department = input()
    obj = Student(name,roll, department)
    lst.append(obj)

for i in lst:
    print(i.Name, i.Roll, i.Department)