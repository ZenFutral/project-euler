# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Answer: 6857

from math import sqrt
from time import time
from statistics import mean
from numpy import arange, insert, int32, ones

def findPrimes(upperBound : int):
    primeArray = arange(3, upperBound, 2, dtype = int32)       # 3, 5, 7, 9, 11...upperBound 

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
        
def findLargestFactor(primeArray : any, intToFactor : int):
    primeList = list(primeArray)
    primeList.reverse() # It's fastest to start from the largest numbers

    for prime in primeList:
        # Have to convert to float to avoid:
            # OverflowError: Python int too large to convert to C long
        if intToFactor % float(prime) == 0:
            return prime

def run(intToFactor : int):
    # Sqrt(number) is the largest prime needed to test another prime
    print(f"Number to factor: {intToFactor}")
    upperBound = int(sqrt(intToFactor) + 1 )  
    print(f"Upperbound: {upperBound}")
    primeArray = findPrimes(upperBound)
    answer = findLargestFactor(primeArray, intToFactor)

    return answer

intToFactor : int = 600851475143

# ================================
# NO PROBLEM LOGIC BELOW THIS LINE
# ================================

runCount = 1
runDurations = []

for count in range(runCount):
    print(f"Run: {count + 1}")
    startTime = time()
    answer = run(intToFactor)
    runDurations.append(time() - startTime)

averageRuntime = mean(runDurations)
print(f"Answer: {answer}")
print(f"Runtime: {round(averageRuntime, 3)}s")
