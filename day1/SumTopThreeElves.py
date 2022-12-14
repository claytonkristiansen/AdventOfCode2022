input = open("input.txt", "r")
lines = input.read().splitlines()

mostElvesCalories = [0]

currCalories = 0
for line in lines:
    if(line == ''):
        mostElvesCalories.append(currCalories)
        currCalories = 0
    else:
        currCalories += int(line, base=10)

mostElvesCalories.sort()
print(mostElvesCalories[-3] + mostElvesCalories[-2] + mostElvesCalories[-1])