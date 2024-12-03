# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Answer: 6857
# Average Runtime: 0.073s

from math                           import sqrt
from custom_modules.script_report   import reporter
from custom_modules.primes          import findPrimesUpTo

        
def findLargestFactor(prime_array : any, int_to_factor : int):      #type: ignore
    primeList: list = list(prime_array)
    primeList.reverse() # It's fastest to start from the largest numbers

    for prime in primeList:

        # Have to convert to float to avoid:
        # OverflowError: Python int too large to convert to C long
        if int_to_factor % float(prime) == 0:
            return prime

def main() -> int:
    int_to_factor : int = 600851475143
    upper_bound = int(sqrt(int_to_factor) + 1 )      # Sqrt(number) is the largest prime needed to test another prime
    prime_array = findPrimesUpTo(upper_bound)
    answer = findLargestFactor(prime_array, int_to_factor)

    return answer

reporter(main_function= main)