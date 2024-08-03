
class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = [] # list of Student Objects
        self.subjects = [] # list of Subject Objects

    def add_student(self, student):
        roll_no = f"{self.name} - {len(self.students)+1}"
        student.set_id = roll_no
        self.students.append(student)
    
    def add_subject(self, subject): # subject ak ta object
        self.subjects.append(subject)

    def take_semister_final(self):
        for subject in self.subjects:
            subject.exam(self.students)
        
        for student in self.students:
            student.calculate_final_grade()
