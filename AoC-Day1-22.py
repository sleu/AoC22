total_foods = []
calories = 0

with open('input1.txt') as i:
    food_list = i.read().splitlines()

for food in food_list:
    if food == '':
        total_foods.append(calories)
        calories = 0
    else:
        calories += int(food)

total_foods.sort(reverse=True)

print("A - Highest Calories: %d" % total_foods[0])
print("B - Total Highest 3: %d" % sum(total_foods[:3]))