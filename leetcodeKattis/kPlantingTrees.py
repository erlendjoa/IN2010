

nrOfSeeds = int(input())
growthTimesInput = input().split(" ")
growthTimes = sorted(growthTimesInput, reverse=True)

dayTimer = 0
print(growthTimes)
for i in range(1, len(growthTimes)+1):
    currentDay = int(growthTimes[i-1])
    if currentDay+i >= dayTimer:
        dayTimer = currentDay+i

print(dayTimer)