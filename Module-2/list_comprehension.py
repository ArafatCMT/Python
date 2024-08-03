numbers = [40, 15, 30, 38, 26, 58, 73, 62, 87, 27]
odds = []

# print(numbers)

for ele in numbers:
    if ele % 2 == 1 and ele % 3 == 0:
        odds.append(ele)

# print(odds)

odds_num = [ele for ele in numbers if ele % 2 == 1 if ele % 3 == 0] # list comprehension
# print(odds_num)


players = ['sakib', 'tamim', 'musfik', 'taskin']
ages = [39, 37, 38, 33]

# age_com = []

# for player in players:
    # print('player : ', player)
    # for age in ages:
        # age_com.append([player,age])

# print(age_com)

age_com = [[player,age] for player in players for age in ages]
print(age_com)






