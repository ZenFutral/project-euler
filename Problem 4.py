# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609
# Average Runtime: 0.065s

from time import time
from statistics import mean
from custom_modules.script_report import reporter


def defineRange(digit_count : int):
    min_num_str: str = "1"
    max_num_str: str = "9"

    for i in range(digit_count - 1):
        min_num_str += "0"
        max_num_str += "9"

    min_num: int = int(min_num_str)
    max_num: int = int(max_num_str)

    bounds: tuple[int, int] = (min_num, max_num)
    return bounds

def testIfPal(number: int):
    num_str: str = str(number)
    return True if num_str == num_str[::-1] else False


def main() -> int:
    pal_list:    list[int]       = []                           # List for palindroms
    bounds:      tuple[int, int] = defineRange(3)               # Creates our lowest and highest number from digit limit
    min_num:     int             = bounds[0] - 1                # -1 to allow for exlusive ranges
    max_num:     int             = bounds[1]
    prime_range: range           = range(max_num, min_num, -1)  # Start testing numbers starting from the largest

    for p_num in prime_range:
        sub_range: range = range(p_num, min_num, -1) # Removes duplicate operations

        for s_num in sub_range:
            num_to_test: int = p_num * s_num

            if testIfPal(num_to_test): # If the num_to_test is a pal, add to our list
                pal_list.append(num_to_test)
    
    answer: int = max(pal_list)
    return answer

reporter(main_function= main)