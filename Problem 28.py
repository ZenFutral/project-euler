# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
# Diagonals: 1, 3, 5, 7, 9, 13, 17, 21, 25
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#
# Answer: 669171001
# Average Runtime: 0.001s

from time import time
from statistics import mean

def getRowCount(numUpdater: int) -> int:
    return numUpdater + 1



def main() -> int:
    running: bool = True
    currentNum: int = 1
    numUpdater: int = 0
    updateTrigger: int = 0
    rowCount: int = 1   # This variable 'jumps-the-gun' and updates it's row count 1 number early (ie. number 9 flags 5th row)
    diagonalInts: list[int] = [1]   # Removes need for advanced logic to handle 1-9 higher count cycle 

    while running == True:  
        if updateTrigger % 4 == 0:  # When currentNum is the highest on ring, advance to next ring
            numUpdater += 2
        
        rowCount = getRowCount(numUpdater)
        if rowCount > 1001:
            running = False
            break

        currentNum += numUpdater
        diagonalInts.append(currentNum)
        
        updateTrigger += 1

    answer: int = sum(diagonalInts)
    return answer

# ================================
# NO PROBLEM LOGIC BELOW THIS LINE
# ================================

runCount: int = 10
runDurations: list[float] = []
startTime: float = time()

if __name__ == '__main__':
    print(f"Executing script {runCount} times...")
    for count in range(runCount):
        answer: int = main()
        print(f"Run: {count} --- Answer: {answer} --- Total Runtime: {round(time() - startTime, 1)}s", end="\r")

    averageRuntime: float = (time() - startTime) / runCount
    print(f"Executing Finished --- Answer: {answer} --- Average Runtime: {round(averageRuntime, 3)}s --- Total Runtime: {round(time() - startTime, 3)}s")
    
