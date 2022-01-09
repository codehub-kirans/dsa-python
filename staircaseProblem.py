def numberOfSteps(totalSteps):
    #Possible steps allowed are 1, 2 & 3

    if totalSteps <= 0:
        return 0
    elif totalSteps == 1:
        return 1
    elif totalSteps == 2:
        return 2
    elif totalSteps == 3:
        return 4

    return numberOfSteps(totalSteps - 1) + numberOfSteps(totalSteps - 2) + numberOfSteps(totalSteps - 3)

#test Staircase Problem
print(numberOfSteps(5))