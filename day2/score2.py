def Score(inpString):
    pair = inpString.split(' ')
    if(pair[0] == "A" and pair[1] == "X"):      #Rock and Lose          choose: Scissors
        return 3
    elif(pair[0] == "A" and pair[1] == "Y"):    #Rock and Draw          choose: Rock
        return 4
    elif(pair[0] == "A" and pair[1] == "Z"):    #Rock and Win           choose: Paper
        return 8
    elif(pair[0] == "B" and pair[1] == "X"):    #Paper and Lose         choose: Rock
        return 1
    elif(pair[0] == "B" and pair[1] == "Y"):    #Paper and Draw         choose: Paper
        return 5
    elif(pair[0] == "B" and pair[1] == "Z"):    #Paper and Win          choose: Scissors
        return 9
    elif(pair[0] == "C" and pair[1] == "X"):    #Scissors and Lose      choose: Paper
        return 2
    elif(pair[0] == "C" and pair[1] == "Y"):    #Scissors and Draw      choose: Scissors
        return 6
    elif(pair[0] == "C" and pair[1] == "Z"):    #Scissors and Win       choose: Rock
        return 7

input = open("input.txt")
lines = input.read().splitlines()

totalScore = 0
for line in lines:
    totalScore += Score(line)

print(totalScore)