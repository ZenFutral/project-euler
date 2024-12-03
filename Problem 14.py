# The following iterative sequence is defined for the set of positive integers:
#  n -> n/2 (n is even)
#  n -> 3n+1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
#   13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), is is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
#
# Answer: 837799
# Average Runtime: 33.03s

from custom_modules.script_report import reporter


def main() -> int:
    collatzCountsDict: dict[int, int] = {}

    for startingNum in range(1, 1000000 + 1):
        currentNum: int = startingNum
        collatzSequence: list[int] = [startingNum]

        while currentNum > 1:
            if currentNum % 2 ==0:
                currentNum = int(currentNum / 2)
                collatzSequence.append(currentNum)
            
            else:
                currentNum = (3 * currentNum) + 1
                collatzSequence.append(currentNum)

        collatzCountsDict[startingNum] = len(collatzSequence)

    v = list(collatzCountsDict.values())
    k = list(collatzCountsDict.keys())
    answer = k[v.index(max(v))]
    return answer

reporter(main_function= main)