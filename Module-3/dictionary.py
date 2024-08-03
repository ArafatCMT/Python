# dictionary holo key value pair
# dictionary te value rakte holo jorai jorai rakte hobe

person = {
    "Name" : "Arafat Hossain Emon",
    "Roll" : 527455,
    "Department" : "Computer Technology",
    "Collage" : "Pabna Politechnic, Institute",
    "Session" : "20-21",
    "Semmester" : "Seventh"
}

# print(person)

print(person["Name"]) # access item
print(person["Department"])
print(person.get("Session"))
print(person.keys())
person["Semmester"] = "Eight" #change item
print(person.get("Semmester"))
print(person.get("Session")) # access item

person["Nationality"] = "Bangladeshi" # add item
print(person)

person.pop("Semmester") # item remove from dictionary
person.popitem() # last item remove from dictionary
print(person)

# loop dictonary
# for item in person:
#     print(item , ":" ,person[item])

# for key , value in person.items():
#     print(key, ":", value)

# copy dictionary

myDict = person.copy()
for item in myDict:
    print(item, ":", myDict[item])