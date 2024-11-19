# n! means n x (n-1) x...x 3 x 2 x 1
# For example, 10! = 10 x 9 x...x 3 x 2 x 1 = 3628800
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
# Find the sum of the digits in the number 100!.
# Answer: 648
# Average Runtime: 0.0s

from math import factorial
from time import time
from statistics import mean


def run():
    number = 100
    factorialAnswer = factorial(number)

    answer = 0
    for digit in str(factorialAnswer):
        answer += int(digit)

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
    
