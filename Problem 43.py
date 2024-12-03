# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the first digit, and d2 be the second digit, and so on. In this way, we not the following:
#   d2d3d4 = 406 is divisible by 2
#   d3d4d5 = 063 is divisible by 3
#   d4d5d6 = 635 is divisible by 5
#   d5d6d7 = 357 is divisible by 7
#   d6d7d8 = 572 is divisible by 11
#   d7d8d9 = 728 is divisible by 13
#   d8d9d10 = 289 is divisible by 17

# Find the sum of all 0 to 9 pandigital numbers with this property. 

# Answer: 16695334890
# Average Runtime: 5.601s

from custom_modules.script_report import reporter
from itertools import permutations

idx_key_dict: dict[tuple[int, int], int] = {
    (1, 4): 2,
    (2, 5): 3,
    (3, 6): 5,
    (4, 7): 7,
    (5, 8): 11,
    (6, 9): 13,
    (7, 10): 17 
}

def hasTrait(number : str) -> bool:
    for key, value in idx_key_dict.items():

        idx_as_int: int = int(number[key[0]:key[1]])

        if idx_as_int % value == 0:
            continue

        else:
            return False
    
    return True

def get0To9Pandigitals() -> set[str]:
    digit_str: str = '0123456789'
    set_of_pandigs: set[str] = {''.join(p) for p in permutations(digit_str)}
    return set_of_pandigs

def main() -> int:
    set_of_pandigs: set[str] = get0To9Pandigitals()
    pandigs_with_trait: list[str] = [i for i in list(set_of_pandigs) if hasTrait(i)]
    pandig_ints: list[int] = [int(i) for i in pandigs_with_trait]
    answer: int = sum(pandig_ints)
    return answer

reporter(main_function= main)