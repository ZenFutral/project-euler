from math import factorial

def run():
    number = 100
    factorialAnswer = factorial(number)

    answer = 0
    for digit in str(factorialAnswer):
        answer += int(digit)

    return answer


answer = run()
print(answer)