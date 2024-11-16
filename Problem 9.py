# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# Answer: 31875000

'''
from math import sqrt

triCir = 50
c = triCir/2
b = 2

while True:
    sqrA = int(c - (b * b))

    if sqrA <= 0:
        print('ERROR: Less Than Zero')
        break

    a = sqrt(sqrA)

    if str(a)[-2:] == '.0':
        break

    b += 1

c = sqrt(c)

print(a,b,c)'''

from math import sqrt, prod

def findTriplets(targetNumber : int):

    for a in range(1, targetNumber):
        for b in range(1, targetNumber):
            aSqr : int = a * a
            bSqr : int = b * b
            cSqr : int = aSqr + bSqr
            c : any = sqrt(cSqr)
            
            tripletTuple : tuple[int, int, int] = (int(a), int(b), int(c))
            
            if c % 1 == 0:
                if sum(tripletTuple) == targetNumber:
                    return tripletTuple
                
                elif sum(tripletTuple) > 1000:
                    break 
    
    return -1


def run():
    targetNumber : int = 1000
    tripletTuple : tuple[int, int, int] = findTriplets(targetNumber)
    answer : int = prod(tripletTuple)

    print(answer)



run()
