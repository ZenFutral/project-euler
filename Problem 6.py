# The sum of the squares of the first ten natural numbers is,
# (1^2) + (2^2) +...+ (10^2) = 385
# 
# The square of the sum of the first ten natural numbers is, 
# (1 + 2 +...+ 10)^2 = 55^2 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
# Answer: 25164150
# Average Runtime: 0.0s

from custom_modules.script_report import reporter

def getSumOfSquares(limit: int) -> int:
    sqr_list:   list[int]   = [i*i for i in range(1, limit + 1)]
    sum_of_sqr: int         = sum(sqr_list)
    return sum_of_sqr

def getSquareOfSum(limit: int) -> int:
    sqr_list:       list[int]   = [i for i in range(1, limit + 1)]
    sum_of_list:    int         = sum(sqr_list)
    sqr_of_sum:     int         = sum_of_list * sum_of_list
    return sqr_of_sum

def main() -> int:
    limit:      int = 100
    sum_of_sqr: int = getSumOfSquares(limit)
    sqr_of_sum: int = getSquareOfSum(limit)

    answer:     int = sqr_of_sum - sum_of_sqr
    return answer

reporter(main_function= main)