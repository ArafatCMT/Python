class Attend:
    def __init__(self, subject, attendance='A'):
        self.subject = subject
        self.attendance = attendance

    def Get_marks(self):
        if self.attendance == 'P':
            from random import randint
            print(randint(30,91))
        else:
            print(f'you don\'t attend the exam')

rahim = Attend('English', 'P')
rahim.Get_marks()

karim = Attend('Physics')
karim.Get_marks()
