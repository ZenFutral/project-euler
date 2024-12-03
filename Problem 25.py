# The Fibonacci sequence is defined by the recurrence relation:
# Fn = F(n-1) + F(n-2) where F1 = 1 and F2 = 1.
# 
# Hence the first 12 terms will be:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# 
# The 12th term, F12, is the first term to contain three digits
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
# 
# Answer: 4782
# Average Runtime: 0.029s

from custom_modules.script_report import reporter

def main() -> int:
    fib_list:     list[int] = [1, 1]
    last_fib_len: int       = 1
    
    while last_fib_len < 1000:
        f1: int = fib_list[-1]
        f2: int = fib_list[-2]
        f3: int = f1 + f2
        
        last_fib_len = len(str(f3))

        fib_list.append(f3)

    answer: int = len(fib_list)
    return answer

reporter(main_function= main)