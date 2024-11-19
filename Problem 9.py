# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Answer: 31875000
# Average Runtime: 0.1s

from time import time
from statistics import mean
from math import sqrt, prod

def findTriplets(targetNumber : int):
    for a in range(1, targetNumber):
        for b in range(1, targetNumber):
            aSqr = a * a
            bSqr = b * b
            cSqr = aSqr + bSqr
            c : any = sqrt(cSqr)
            
            tripletTuple = (int(a), int(b), int(c))
            
            if c % 1 == 0:
                if sum(tripletTuple) == targetNumber:
                    return tripletTuple
                
                elif sum(tripletTuple) > 1000:
                    break 
    
    return -1


def run():
    targetNumber = 1000
    tripletTuple = findTriplets(targetNumber)
    answer = prod(tripletTuple)
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
    
