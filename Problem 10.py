# The sum of the primes below 10 is 2 + 3 + 5 + 7 =17.
# Find the sum of all the primes below two million.
#
# Answer: 142913828922
# Average Runtime: 0.321s

from time import time
from statistics import mean
from numpy import arange, ones, insert

def findPrimes(upperBound : int):
    primeArray = arange(3, upperBound, 2)       # 3, 5, 7, 9, 11...upperBound 

    # Since our prime array starts at 3, if we begin elimanating multiples and iterate by a step each time, we should always have a prime next
    # Therefor, prime conditions are that it is not divisable by a divisor OR it is the number being tested

    is_prime = ones(len(primeArray), dtype=bool)

    for i, number in enumerate(primeArray):
        if is_prime[i]:  # Check if the number is still a potential prime
            # Filter out multiples of the current prime
            is_prime[i+number::number] = False
    
    # Applies bool mask to initial array
    primeArray = primeArray[is_prime]

    # Inserts 2 at the begining, since we skipped that originally.
    primeArray = insert(primeArray, 0, 2)
    return primeArray

def run():
    targetNumber = 2000000
    primeList = findPrimes(targetNumber)
    answer = sum(primeList)
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
    
