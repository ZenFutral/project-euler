# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 233168
# Average Runtime: 0.002s

from time import time
from statistics import mean

runCount = 10
runDurations = []

def run():
    limit : int = 1000
    divisors : tuple[int] = (3, 5)
    multiples : list[int] = []


    [[multiples.append(num) for divisor in divisors 
        if (num % divisor == 0) and (num not in multiples)] 
        for num in range(limit)]

    answer : int = sum(multiples)
    return answer


for count in range(runCount):
    startTime = time()
    answer = run()
    runDurations.append(time() - startTime)

averageRuntime = mean(runDurations)
print(f"Answer: {answer}")
print(f"Runtime: {round(averageRuntime, 3)}s")
