# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# Answer: 233168

# I wanted to use this problem as an excuse to jam everything into nested list comprehension.

limit = 1000
divisors = (3, 5)
multiples = []


[[multiples.append(num) for divisor in divisors 
    if (num % divisor == 0) and (num not in multiples)] 
    for num in range(limit)]

answer = sum(multiples)

print(answer)
