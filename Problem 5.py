
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisable by all of the numbers from 1 to 20?
# Answer: 232792560
# Average Runtime: 1.308s

from custom_modules.script_report import reporter

def main() -> int:
    max_div:        int = 20
    num_to_test:    int = 0

    while True:
        num_to_test += max_div  # Counting by the max_div maximized how many numbers we can skip

        # Don't need to test by max divider, since every number we test is already divisable by max_div
        # Counts backwards in an attempt to be faster
        for divider in range(max_div - 1, 1, -1):  

            if num_to_test % divider != 0:  # If num_to_test doesn't divide evenly by divider, try next number   
                break

            elif divider == 2:
                answer: int = num_to_test
                return answer

reporter(main_function= main)