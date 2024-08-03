class Student:
    def __init__(self, name, cls, id) -> None:
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
        self.Student = []
        self.Teacher = []

    def Add_to_teacher(self, name, subject):
        id = len(self.Teacher) + 101
        teacher = Teacher(name, subject, id)
        self.Teacher.append(teacher)

    def Enroll(self, name):
        id = len(self.Student) + 1
        student = Student(name, 'Python', id)
        self.Student.append(student)

    def __repr__(self) -> str:
        print(f'Welcome to , {self.name} learning institute')
        print()
        print('-- * -- * -- * -- * -- Our Teachers -- * -- * -- * -- * --')
        print()
        for i in self.Teacher:
            print(i)
        print()
        print('-- * -- * -- * -- * -- Our Students -- * -- * -- * -- * --')
        for i in self.Student:
            print(i)


Phitron = School('Phitron')
Phitron.Enroll('Arafat')
Phitron.Enroll('Jannat')
Phitron.Enroll('Mithila')
Phitron.Enroll('Hasan')
Phitron.Enroll('Hamim')

Phitron.Add_to_teacher('Rahat Khan', 'C++')
Phitron.Add_to_teacher('Ramjan Ali', 'C')
Phitron.Add_to_teacher('Shakib Khan', 'DS')

print(Phitron)

