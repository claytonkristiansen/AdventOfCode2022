def Score(inpString):
    pair = inpString.split(' ')
    if(pair[0] == "A" and pair[1] == "X"):
        return 4
    elif(pair[0] == "A" and pair[1] == "Y"):
        return 8
    elif(pair[0] == "A" and pair[1] == "Z"):
        return 3
    elif(pair[0] == "B" and pair[1] == "X"):
        return 1
    elif(pair[0] == "B" and pair[1] == "Y"):
        return 5
    elif(pair[0] == "B" and pair[1] == "Z"):
        return 9
    elif(pair[0] == "C" and pair[1] == "X"):
        return 7
    elif(pair[0] == "C" and pair[1] == "Y"):
        return 2
    elif(pair[0] == "C" and pair[1] == "Z"):
        return 6

input = open("input.txt")
lines = input.read().splitlines()

totalScore = 0
for line in lines:
    totalScore += Score(line)

print(totalScore)