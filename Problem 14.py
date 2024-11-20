# The following iterative sequence is defined for the set of positive integers:
#  n -> n/2 (n is even)
#  n -> 3n+1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), is is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Answer: 837799
# Average Runtime: 33.03s

from time import time
from statistics import mean


def main() -> int:
    collatzCountsDict: dict[int, int] = {}

    for startingNum in range(1, 1000000 + 1):
        currentNum: int = startingNum
        collatzSequence: list[int] = [startingNum]

        while currentNum > 1:
            if currentNum % 2 ==0:
                currentNum = int(currentNum / 2)
                collatzSequence.append(currentNum)
            
            else:
                currentNum = (3 * currentNum) + 1
                collatzSequence.append(currentNum)

        collatzCountsDict[startingNum] = len(collatzSequence)

    v = list(collatzCountsDict.values())
    k = list(collatzCountsDict.keys())
    answer = k[v.index(max(v))]
    return answer

# ================================
# NO PROBLEM LOGIC BELOW THIS LINE
# ================================

runCount: int = 10
runDurations: list[float] = []
masterStart: float = time()

if __name__ == '__main__':
    for count in range(runCount):
        print(f"Run: {count + 1} --- Current Runtime: {round(time() - masterStart, 1)}")
        startTime: float = time()
        answer = main()
        runDurations.append(time() - startTime)

    averageRuntime = mean(runDurations)
    print("===================")
    print(f"Answer: {answer}")
    print(f"Runtime: {round(averageRuntime, 3)}s")
    
