# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20 x 20grid?
# 
# Answer: 137846528820
# Average Runtime: 0.000s

from custom_modules.script_report import reporter
from math import factorial


def main() -> int:
    grid_width: int = 20
    total_moves: int = grid_width + grid_width
    
    answer: int = int(factorial(total_moves) / (factorial(grid_width) * factorial(grid_width)))

    return answer

reporter(main_function= main)
    
