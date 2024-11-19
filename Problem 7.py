# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?
# Answer: 104743
# Average Runtime: 3.372s

from time import time
from statistics import mean

def isPrime(number : int, primeList : int):       
    for prime in primeList:
        if number % prime == 0:
            return False
        
    if number == 1:
        return False
    
    return True

def findPrimes(targetLength : int):
    primeList : list[int] = [2, 3]
    numberToTest : int = 3

    while len(primeList) < targetLength:
        numberToTest += 2

        if isPrime(numberToTest, primeList):
            primeList.append(numberToTest)
                             
    return primeList

def run(targetLength : int):
    primeList : list[int] = findPrimes(targetLength)

    answer : int = primeList[-1]
    return answer

# ================================
# NO PROBLEM LOGIC BELOW THIS LINE
# ================================

runCount = 10
runDurations = []

for count in range(runCount):
    print(f"Run: {count + 1}")
    startTime = time()
    answer = run(10001)
    runDurations.append(time() - startTime)

averageRuntime = mean(runDurations)
print(f"Answer: {answer}")
print(f"Runtime: {round(averageRuntime, 3)}s")
    
