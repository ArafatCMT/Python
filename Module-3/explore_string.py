word1 = "Python is a \"Programming\" Language" # use escape character \"
word2 = 'computer technology'
word3 = """
    Python is a "Programming" Language.
    I went ot learn python
"""

print(word1)
# print(word2)
# print(word3)

#word1[5] = "M" # string immutable means you can not change it
# print(word1[5])

# slice string 

print(word1[3:8]) 
print(word1[-5])
print(word1[::-1]) #  reverse string 
print(word1)
print(word1[2:10:2])
print(word1[10])

# string method

#convert string lower case
print(word1)
# print(word1.lower())

#convert string upper case
# print(word1.upper())

#convert strin in title case
# print(word1.title())

# swap case
# print(word1.swapcase())

# print(word2.capitalize())

# if 'is' in word1:
#     print("exits")

# print(word1.find('is'))

# format

day = 2
month = "April"
year = 2024

print("Today {0} {1} {2}".format(day,month,year))
print(f"Today {day} {month} {year}")