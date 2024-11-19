# 2^15 = 32768 and the fum of it's digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000.

# Answer: 1366
# Average Runtime: 0.0s

from time import time
from statistics import mean

def run():
    power = 1000
    number = 2 ** power
    digitStringList = list(str(number))

    digitIntList = [int(i) for i in digitStringList]
    answer = sum(digitIntList)

    return answer

# ================================
# NO PROBLEM LOGIC BELOW THIS LINE
# ================================

runCount = 10
runDurations = []

for count in range(runCount):
    print(f"Run: {count + 1}")
    startTime = time()
    answer = run()
    runDurations.append(time() - startTime)

averageRuntime = mean(runDurations)
print(f"Answer: {answer}")
print(f"Runtime: {round(averageRuntime, 3)}s")
    
