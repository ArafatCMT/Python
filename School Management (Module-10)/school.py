class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {} # {"subject" : teacher_object}
        self.classrooms = {} # {"eight" : classroom_object}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
    
    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return 'A+'
        elif marks >= 70 and marks <= 79:
            return 'A'
        elif marks >= 60 and marks <= 69:
            return 'A-'
        elif marks >= 50 and marks <= 59:
            return 'B'
        elif marks >= 40 and marks <= 49:
            return 'C'
        elif marks >= 33 and marks <= 39:
            return 'D'
        else:
            return 'F'
    
    @staticmethod
    def grade_ot_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00,
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value == 5.00:
            return 'A+'
        elif value >= 4.00 and value < 5.00:
            return 'A'
        elif value >= 3.50 and value < 4.00:
            return 'A-'
        elif value >= 3.00 and value < 3.50:
            return 'B'
        elif value >= 2.00 and value < 3.00:
            return 'C'
        elif value >= 1.00 and value < 2.00:
            return 'D'
        else:
            return 'F'
        
    def __repr__(self):
        # all classroom
        print("All ClassRooms:")
        for key in self.classrooms.keys():
            print(key)

        # all students
        print("All Students:")
        result = ''
        for key,value in self.classrooms.items():
            result += f"{key.upper()} ClassRooms Students\n"
            
            for student in value.students:
                result += f"{student.name}\n"
        print(result)

        # all subjects
        subject = ''
        for key,value in self.classrooms.items():
            subject += f"Class {key.upper()} Subjects:\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)

       # all teachers - homework
        print("All Teachers:")
        res = ''
        for key,value in self.teachers.items():
            res += f"{key} Subject Teacher\n"
            
            res += f"{value.name}\n"
        print(res)
       
       # all students results
        print("Student Results:")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name, k, i, student.subject_grade[k])
                print(student.calculate_final_grade())
        return ''