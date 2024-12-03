# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
# Diagonals: 1, 3, 5, 7, 9, 13, 17, 21, 25
# 
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
#
# Answer: 669171001
# Average Runtime: 0.001s

from custom_modules.script_report import reporter

def getRowCount(num_modifier: int) -> int:
    return num_modifier + 1

def main() -> int:
    running:        bool = True
    current_num:    int = 1
    num_modifier:   int = 0
    while_counter:  int = 0
    row_count:      int = 1   # This variable 'jumps-the-gun' and updates it's row count 1 number early (ie. number 9 flags 5th row)
    diagonal_ints:  list[int] = [1]   # Removes need for advanced logic to handle 1-9 higher count cycle 

    while running == True:  
        if while_counter % 4 == 0:  # When current_num is the highest on ring, advance to next ring
            num_modifier += 2
        
        row_count = getRowCount(num_modifier)
        if row_count > 1001:
            running = False
            break

        current_num += num_modifier
        diagonal_ints.append(current_num)
        
        while_counter += 1

    answer: int = sum(diagonal_ints)
    return answer

reporter(main_function= main)