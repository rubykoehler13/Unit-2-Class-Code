cat_age = int(input("How old is your cat? "))
kitten = cat_age <= 6
teen = cat_age <= 11
adult = cat_age < 86
senior = cat_age >= 86

print("Approach #1: ")
if kitten:
    print("Kitten - Price $250")
elif teen:
    print("Teenager - Price: $225")
elif adult:
    print("Adult - Price: $150")
elif senior:
    print("Senior - Price: $85")

print("Approach #2: ")
if senior:
    print("Senior - Price: $85")
elif adult:
    print("Adult - Price: $150")
elif teen:
    print("Teenager - Price: $225")
elif kitten:
    print("Kitten - Price: $250")

print("Approach #3: ")
if kitten:
    print("Kitten - Price: $250")
if teen:
    print("Teenager - Price: $225")
if adult:
    print("Adult - Price: $150")
if senior:
    print("Senior - Price: $85")

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
# I believe that if you do 'if' statements, they will just print all 