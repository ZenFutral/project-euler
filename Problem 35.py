# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100:
# 2, 3, 5, 7, 11, 13, 17, 31, 71, 73, 79, and 97
# How many circular primes are there below one million?
# 
# Answer: 55
# Average Runtime: 0.186s

from custom_modules.script_report import reporter
from custom_modules.primes        import findPrimesUpTo



def rotateNumber(prime_string: str) -> str:
    if len(prime_string) > 1:
        rotated_prime: str = prime_string[1:] + prime_string[0]

    else:
        rotated_prime = prime_string

    return rotated_prime

def testIfCircular(prime: str, prime_string_set: set[str]) -> bool:
    for _ in range(len(prime)):
        prime = rotateNumber(prime)

        if prime not in prime_string_set:
            return False
    
    return True

def findCircularPrimes(prime_list: list[int]) -> list[str]:
    prime_string_set: set[str] = {str(p) for p in prime_list}
    circular_primes:   list[str] = []

    for prime in prime_string_set:

        is_circular: bool = testIfCircular(prime, prime_string_set)
        
        if is_circular:
            circular_primes.append(prime)
    
    return circular_primes

def main() -> int:
    target_number:      int       = 1000000
    prime_list:         list[int] = findPrimesUpTo(target_number)
    circular_primes:    list[str] = findCircularPrimes(prime_list)

    answer: int = len(circular_primes)
    return answer

reporter(main_function= main)