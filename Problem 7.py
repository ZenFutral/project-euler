# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?
# Answer: 104743
# Average Runtime: 0.032s (*0.011s)
# Adjusting {upper_bound_modifier} leads to much faster time

from custom_modules.script_report import reporter
from custom_modules.primes        import findNthPrime

def main() -> int:
    target_length: int = 10001
    
    prime_list: list[int] = findNthPrime(length= target_length, upper_bound_modifier=105000)

    answer: int = prime_list[-1]
    return answer

reporter(main_function= main)