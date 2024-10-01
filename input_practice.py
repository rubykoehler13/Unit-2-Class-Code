ingredient_1 = input("What is the first ingredient you'd like in your salad? ")
ingredient_2 = input("What is the second ingredient you'd like in your salad? ")
ingredient_3 = input("What is the third ingredient you'd like in your salad? ")

oz_1 = float(input(f"How many ounces of {ingredient_1} would you like for one serving of salad? "))
oz_2 = float(input(f"How many ounces of {ingredient_2} would you like for one serving of salad? "))
oz_3 = float(input(f"How many ounces of {ingredient_3} would you like for one serving of salad? "))

serving_num = int(input("How many servings would you like the salad to make? "))

total_ingredient_1 = (oz_1*serving_num)
total_ingredient_2 = (oz_2*serving_num)
total_ingredient_3 = (oz_3*serving_num)

print(f"Total oz of {ingredient_1} needed for {serving_num} servings is: {total_ingredient_1}")
print(f"Total oz of {ingredient_2} needed for {serving_num} servings is: {total_ingredient_2}")
print(f"Total oz of {ingredient_3} needed for {serving_num} servings is: {total_ingredient_3}")