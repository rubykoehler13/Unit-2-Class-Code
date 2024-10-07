'''
Name: Ruby Koehler
Date: 10/1/24
Description: Unit 2 Homework 1
'''

print("Problem 1".center(20,"-"))

print(" ")
print("Idea 1: User navigating through an abandoned house.")
print("Idea 2: User has to survive on desert island.")
print("Idea 3: User has to reach the top of a mountain.")

print("Problem 2".center(20,"-"))

Title = r"""
________                               __    .___       .__                     .___
\______ \   ____   ______ ____________/  |_  |   | _____|  | _____    ____    __| _/
 |    |  \_/ __ \ /  ___// __ \_  __ \   __\ |   |/  ___/  | \__  \  /    \  / __ |
 |____`   \  ___/ \___ \\  ___/|  | \/|  |   |   |\___ \|  |__/ __ \|   |  \/ /_/ |
/_______  /\___  >____  >\___  >__|   |__|   |___/____  >____(____  /___|  /\____ |
        \/     \/     \/     \/                       \/          \/     \/      \/
"""
print(Title)

print("Problem 3".center(20,"-"))

distance = 173.8
user_mpg = int(input("How many miles per gallon does your car get?"))
gas_price = float(input("How much does one gallon of gas near you cost? $"))
gas_gallon = int(input("How many gallons of gas does your car hold?"))
price_full_tank = (gas_gallon*gas_price)
# Assuming the user's car is completely empty
total_trip_cost = (((distance/user_mpg)/gas_gallon)*price_full_tank)
print(f"The total cost for you to drive from Portland to Seattle is ${total_trip_cost}")