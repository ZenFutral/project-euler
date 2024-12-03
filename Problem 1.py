# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 233168
# Average Runtime: 0.001s

from custom_modules.script_report import reporter

def main() -> int:
    limit:      int             = 1000
    divisors:   tuple[int, int] = (3, 5)
    multiples:  list[int]       = []


    [[multiples.append(num) for divisor in divisors #type: ignore   # Append a number to list           
        if (num % divisor == 0) and (num not in multiples)]         # If that number perfectly divides and not already in list
        for num in range(limit)]                                    # Do this for every number until limit is reached

    answer: int = sum(multiples)
    return answer

reporter(main_function= main)
