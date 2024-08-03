class Student:
    name = "Arafat"
    roll = 527455
    department = "Computer Technology"

    def institute(self):
        print("Pabna Polytechnic Institute")

    def send_sms(self, phone, sms):
        print(f"Sending sms to : {phone} and message : {sms}")

person = Student()
print(person.name, person.roll, person.department)
person.institute()
person.send_sms(173882,"I love you, Python")