# 2^15 = 32768 and the fum of it's digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000.

# Answer: 1366

def run():
    power = 1000
    number = 2 ** power
    digitStringList = list(str(number))

    digitIntList = [int(i) for i in digitStringList]
    answer = sum(digitIntList)

    return answer

answer = run()
print(answer)
