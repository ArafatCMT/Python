def full_name(fast_name, last_name):
    name = f"{fast_name} {last_name}"
    # name = fast_name + " " + last_name
    return name

# name = full_name(last_name = "Hossain", fast_name = "Arafat")
# print(name)


# def famous(fast_name, last_name, **addition):
#     name = f"{fast_name} {last_name}"
#     # print(addition['profession'])

#     for key, value in addition.items():
#         print(key,value)
#     return name

# name = famous(designation = "Dr", last_name = "Alim", fast_name = "Abdul" , profession = "Professor" )
# print(name)


#return multiple things in function

def a_lot(num1, num2):
    sum = num1 + num2
    mult = num1 * num2
    mod = num1 % num2
    # return [sum, mult, mod]
    return sum, mult, mod

everythings = a_lot(5,2)
print(everythings)




