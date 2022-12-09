totalfoods = []

with open('input1.txt') as i:
    food = i.read().splitlines()

calories = 0
for item in food:
    if item == '':
        totalfoods.append(calories)
        calories = 0
    else:
        calories += int(item)

totalfoods.sort(reverse=True)

print("A - Highest Calories: %d" % totalfoods[0])
print("B - Total Highest 3: %d" % sum(totalfoods[:3]))