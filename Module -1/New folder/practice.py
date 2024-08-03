mark = int(input("Enter your mark : "))

if mark >= 80 and mark <= 100:
    print("Your Grade is A+")
elif mark >= 70 and mark <= 79:
    print("Your Grade is A")
elif mark >= 60 and mark <= 69:
    print("Your Grade is A-")
elif mark >= 50 and mark <= 59:
    print("Your Grade is B")
elif mark >= 40 and mark <= 49:
    print("Your Grade is C")
else:
    print("Your Grade is F")