# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Answer: 6857

from math import sqrt

def isPrime(number : int, primeList : int):       
    for prime in primeList:
        if number % prime == 0:
            return False
        
    if number == 1:
        return False
    
    return True

def findPrimes(upperBound : int):
    primeList : list[int] = [2, 3]
    [primeList.append(i) for i in range(1, upperBound, 2) if isPrime(i, primeList)] # Only uses odd numbers
    primeList.insert(0, 2)  # Adds 2 to the begining since we skipped it

    return primeList

def findLargestFactor(primeList : list[int], intToFactor : int):
    primeList.reverse() # It's fastest to start from the largest numbers

    for prime in primeList:
        if intToFactor % prime == 0:
            return prime

def run(intToFactor : int):
    upperBound : int = int(sqrt(intToFactor) + 1 )   # Defines the largest possible prime factor for a int, adds 1 for exclusive iteration

    primeList : list[int] = findPrimes(upperBound)
    answer : int = findLargestFactor(primeList, intToFactor)

    print(answer)

intToFactor : int = 600851475143

run(intToFactor)

