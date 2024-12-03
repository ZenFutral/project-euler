# n! means n x (n-1) x...x 3 x 2 x 1
# For example, 10! = 10 x 9 x...x 3 x 2 x 1 = 3628800
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
# Find the sum of the digits in the number 100!.
#
# Answer: 648
# Average Runtime: 0.000s

from math import factorial
from custom_modules.script_report import reporter

def main() -> int:
    number: int = 100
    factorial_of_number: int = factorial(number)

    answer: int = 0
    for digit in str(factorial_of_number):
        answer += int(digit)

    return answer

reporter(main_function= main)