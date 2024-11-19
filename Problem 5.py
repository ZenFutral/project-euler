
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisable by all of the numbers from 1 to 20?
# Answer: 232792560
# Average Runtime: 2.866s

from time import time
from statistics import mean


def run():
    maxDivider = 20
    numberToTest = 0
    while True:
        numberToTest += maxDivider  # Counting by the maxDivider maximized how many numbers we can skip

        # Don't need to test by max divider, since every number we test is already divisable by maxDivider
        # Counts backwards in an attempt to be faster
        for divider in range(maxDivider - 1, 1, -1):  

            if numberToTest % divider != 0:  # If numberToTest doesn't divide evenly by divider, try next number   
                break

            elif divider == 2:
                answer = numberToTest
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
    
