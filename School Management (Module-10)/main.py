from school import School
from person import Student,Teacher
from subject import Subject
from classroom import ClassRoom

school = School("ABCD", "Dhaka")

# adding class room
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# adding student
rahim = Student("Rahim", eight)
karim = Student("Karim", nine)
fahim = Student("Fahim", ten)
hamim = Student("Hamim", ten)

school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(fahim)
school.student_admission(hamim)

# adding teachers
abul = Teacher("Abul Kalam")
babul = Teacher("Babul Khan")
kabul = Teacher("Kabul Islam")


# adding Subject
 
bangla = Subject("Bangla", abul)
math = Subject("Math", kabul)
physics = Subject("Physics", babul)
chemistry = Subject("Chemistry", kabul)

eight.add_subject(bangla)
eight.add_subject(math)
nine.add_subject(math)
nine.add_subject(physics)
nine.add_subject(chemistry)
ten.add_subject(bangla)
ten.add_subject(math)
ten.add_subject(physics)
ten.add_subject(chemistry)

school.add_teacher(bangla.name, abul)
school.add_teacher(math.name, kabul)
school.add_teacher(physics.name, babul)
school.add_teacher(chemistry.name, kabul)


eight.take_semister_final()
nine.take_semister_final()
ten.take_semister_final()

print(school)