"""
Name: Ruby Koehler
Date: 9-16/24
Description: Unit 2 Lesson 1 Notes
"""

#Variables - store information

message = "Hello, user"
print(message)

# snake_case - name our variables
user_name = input("What is your name?")
user_id = int(input("Enter your id: "))

# variable type command
# print(type(user_name))

# Type 1: Strings
# You can use ' or " to indicate string - be consistent

# f-strings are formatted strings that help with combining string

# Way 1 to combine string: use + (concatenation
# Caution: ll numbers have to have str() around them
message_one = "Welcome" + user_name + "with ID" + str(user_id)
print(message_one)

# Way 2: use f strings
# put variable in curly braces
message_two = f"Welcome {user_name} with ID {user_id}"
print(message_two)

# Possible errors:
# apostrophes inside of single quotes
# resolution: use \ - tells python that the next symbol is literally that thing, it has no Pythonic meaning
famous_quotation = 'Quotations are hard to find in the middle of lessons-it\'s annoying. Mr Smith.'

# raw strings
dog = r"""
            /)-_-(\        /)-_-(\
             (o o)          (o o)
     .-----__/\o/            \o/\__-----.
    /  __      /              \      __  \
\__/\ /  \_\ |/                \| /_/  \ /\__/
     \\     ||                  ||      \\
     //     ||                  ||      //
     |\     |\                  /|     /|
"""
print(dog)