input = open("input.txt", "r")
lines = input.read().splitlines()

mostElf = 0
mostCalories = 0

currElf = 0
currCalories = 0
for line in lines:
    if(line == ''):
        if(currCalories > mostCalories):
            mostCalories = currCalories
            mostElf = currElf
        currCalories = 0
        currElf += 1
    else:
        currCalories += int(line, base=10)

print(mostElf, mostCalories)