class Student:
    def __init__(self, name, cls, id):
        self.name = name
        self.cls = cls
        self.id = id

    def __repr__(self) -> str:
        return f'name : {self.name} , class : {self.cls} , id : {self.id}'

class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name 
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'name : {self.name} , subject : {self.subject} , id : {self.id}'
    

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.Teacher = []
        self.Student = []

    def Add_to_teacher(self, name, subject):
        id = len(self.Teacher) + 101
        teacher = Teacher(name, subject, id)
        self.Teacher.append(teacher)
    
    def Enroll(self, name):
        id = len(self.Student) + 1
        student = Student(name, 'C++', id)
        self.Student.append(student)

    def __repr__(self) -> str:
        print("Welcome to", self.name)
        print()
        print("-*--*--*--*-- OUR Teachers --*--*--*--*-")
        print()
        for i in self.Teacher:
            print(i)
        print()
        print("-*--*--*--*-- OUR Students --*--*--*--*-")
        print()
        for i in self.Student:
            print(i)
        print()
        print("--//--//--//--//--//--//--//--//--//--//--")
        print()



Phitron = School('Phitron')
Phitron.Enroll('Arafat')
Phitron.Enroll('Nahid')
Phitron.Enroll('Omar')
Phitron.Enroll('Taufiq')
Phitron.Enroll('Masud')

Phitron.Add_to_teacher('Naim', 'DS')
Phitron.Add_to_teacher('Rahat', 'Algo')
Phitron.Add_to_teacher('Ramjan', 'C++')

print(Phitron)