# The sum of the primes below 10 is 2 + 3 + 5 + 7 =17.
# Find the sum of all the primes below two million.
#
# Answer: 142913828922
# Average Runtime: 0.163s

from custom_modules.script_report import reporter
from custom_modules.primes        import findPrimesUpTo

def main() -> int:
    target_num: int  = 2000000
    prime_list: list = findPrimesUpTo(target_num)
    answer:     int  = sum(prime_list)
    return answer

reporter(main_function= main)