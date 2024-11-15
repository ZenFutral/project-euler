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


def getSumOfSquares(limit : int):
    squareList : list[int] = [i*i for i in range(1, limit + 1)]
    sumOfSquares : int = sum(squareList)
    return sumOfSquares

def getSquareOfSum(limit : int):
    squareList : list[int] = [i for i in range(1, limit + 1)]
    sumOfList : int = sum(squareList)
    squareOfSum : int = sumOfList * sumOfList
    return squareOfSum


def run(limit = 100):
    sumOfSquares : int = getSumOfSquares(limit)
    squareOfSum : int = getSquareOfSum(limit)

    answer : int = squareOfSum - sumOfSquares
    return answer

answer : int = run()
print(answer)