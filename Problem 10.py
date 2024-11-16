# The sum of the primes below 10 is 2 + 3 + 5 + 7 =17.
# Find the sum of all the primes below two million.
#
# Answer: 142913828922

def isPrime(number : int, primeList : int):       
    for prime in primeList:
        if number % prime == 0:
            return False
        
    if number == 1:
        return False
    
    return True

def findPrimes(targetNumber : int):
    primeList : list[int] = [2, 3]
    numberToTest : int = 3

    while numberToTest < targetNumber:
        numberToTest += 2

        if isPrime(numberToTest, primeList):
            print(numberToTest)
            primeList.append(numberToTest)
                             
    return primeList

def run():
    targetNumber : int = 2000000
    primeList : list[int] = findPrimes(targetNumber)
    answer : int = sum(primeList)
    print(answer)

run()
