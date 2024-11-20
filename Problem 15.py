# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20 x 20grid?
# 
# Answer: 137846528820
# Average Runtime: 

from time import time
from statistics import mean
from math import factorial


def main() -> int:
    gridWidth = 20
    totalMoves = gridWidth + gridWidth
    
    answer: int = int(factorial(totalMoves) / (factorial(gridWidth) * factorial(gridWidth)))

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
    
