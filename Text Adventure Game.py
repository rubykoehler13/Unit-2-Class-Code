'''
Name: Ruby Koehler
Date: 10/14/24
Description: Text Adventure Game
'''

print("Problem 1".center(20,"-"))

print(" ")
print("Idea 1: User navigating through an abandoned house.")
print("Idea 2: User has to survive on desert island.")
print("Idea 3: User has to reach the top of a mountain.")

print("Problem 2".center(20,"-"))

intro_art = r"""
________                               __    .___       .__                     .___
\______ \   ____   ______ ____________/  |_  |   | _____|  | _____    ____    __| _/
 |    |  \_/ __ \ /  ___// __ \_  __ \   __\ |   |/  ___/  | \__  \  /    \  / __ |
 |____`   \  ___/ \___ \\  ___/|  | \/|  |   |   |\___ \|  |__/ __ \|   |  \/ /_/ |
/_______  /\___  >____  >\___  >__|   |__|   |___/____  >____(____  /___|  /\____ |
        \/     \/     \/     \/                       \/          \/     \/      \/
"""
print(intro_art)

user_name = input("Hello. What is your name? ")
print(f"Well, {user_name}, welcome to Desert Island\nLet's see if you can survive...")