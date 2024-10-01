ingredient_1 = input("What is the first ingredient you'd like in your salad? ")
ingredient_2 = input("What is the second ingredient you'd like in your salad? ")
ingredient_3 = input("What is the third ingredient you'd like in your salad? ")
oz_1 = float(input(f"How many ounces of {ingredient_1} would you like for one serving of salad? "))
oz_2 = float(input(f"How many ounces of {ingredient_2} would you like for one serving of salad? "))
oz_3 = float(input(f"How many ounces of {ingredient_3} would you like for one serving of salad? "))
serving_num = input("How many servings would you like the salad to make? ")


print(f"Total oz of {ingredient_1} needed for {serving_num} servings is: ({ingredient_1}*{serving_num})")
print(f"Total oz of {ingredient_2} needed for {serving_num} servings is: ({ingredient_2}*{serving_num})")
print(f"Total oz of {ingredient_3} needed for {serving_num} servings is: ({ingredient_3}*{serving_num})")