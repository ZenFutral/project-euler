# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Answer: 31875000
# Average Runtime: 0.041s

from custom_modules.script_report import reporter
from math import sqrt, prod

def findTriplets(target_num : int) -> tuple[int, int, int]:
    for a in range(1, target_num):
        for b in range(1, target_num):
            a_sqr: int      = a * a
            b_sqr: int      = b * b
            c_sqr: int      = a_sqr + b_sqr
            c: int | float  = sqrt(c_sqr)
            
            triplet_tuple: tuple[int, int, int] = (int(a), int(b), int(c))
            
            if c % 1 == 0:
                if sum(triplet_tuple) == target_num:
                    return triplet_tuple
                
                elif sum(triplet_tuple) > 1000:
                    break 
    
    return (-1, -1, -1)


def main() -> int:
    target_num: int = 1000
    triplet_tuple: tuple[int, int, int] = findTriplets(target_num)
    answer: int = prod(triplet_tuple)
    return answer

reporter(main_function= main)
