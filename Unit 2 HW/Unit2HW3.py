cat_age = int(input("How old is your cat? "))
kitten = cat_age <= 6
teen = cat_age <= 11
adult = cat_age <= 95
senior = cat_age >= 96

print("Approach #1: ")
if kitten:
    print("Kitten - Price $250")
elif teen:
    print("Teenager - Price: $225")
elif adult:
    print("Adult - Price: $150")
elif senior:
    print("Senior - Price: $85")
print("")

print("Approach #2: ")
if senior:
    print("Senior - Price: $85")
elif adult:
    print("Adult - Price: $150")
elif teen:
    print("Teenager - Price: $225")
elif kitten:
    print("Kitten - Price: $250")
print("")

print("Approach #3: ")
if kitten:
    print("Kitten - Price: $250")
if teen:
    print("Teenager - Price: $225")
if adult:
    print("Adult - Price: $150")
if senior:
    print("Senior - Price: $85")
print("")

print("Approach #4: ")
if senior:
    print("Senior - Price: $85")
if adult:
    print("Adult - Price: $150")
if teen:
    print("Teenager - Price: $150")
if kitten:
    print("Kitten - Price: $250")

# I think that only approach #1 works because I tested many different numbers that would give me\n
# (as the user), answers of each: kitten, teenager, adult, and senior, and only approach #1 was right every time.\n
# I believe that if you do 'if' statements every time, they will print all the statements that the value\n
# falls under. For example, let's say the user puts the number 5 in; for the approaches that use all 'if' \n
# statements, the number 5 does fall under each variable, so it will print all: kitten, teenager, adult, \n
# and senior. But when you do 'elif' statements, your code will not keep going once it's met one of the
# variables, but 'elif' statements allow the code to keep searching for the right variable that the \n
# number falls under, without printing all the ones it doesn't fall under.
# Also, if you start with the higher numbers/values (like senior), your number will meet \n
# all of the values once again. If you were to input 10 and had your list going from senior to kitten, \n
# 10 is less than 96, so senior will print, then it goes to adult, and 10 is less than 95, so adult will \n
# print, then it goes to teenager, and once again 10 is less than 11, so it will print teenager. If you \n
# start with the smaller values, such as kitten, the code will go through and test each one, if it meets \n
# one of the first ones, it will not keep going because it's met the smallest possible range, unlike when \n
# you start with the much higher numbers, it will keep going because it meets all the ranges.