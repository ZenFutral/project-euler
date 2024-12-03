# 2^15 = 32768 and the fum of it's digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000.

# Answer: 1366
# Average Runtime: 0.000s

from custom_modules.script_report import reporter

def main() -> int:
    power: int  = 1000
    number: int = 2 ** power
    list_of_digits_as_str: list[str] = list(str(number))

    list_of_digits_as_int: list[int] = [int(d) for d in list_of_digits_as_str]
    answer: int = sum(list_of_digits_as_int)

    return answer

reporter(main_function= main)