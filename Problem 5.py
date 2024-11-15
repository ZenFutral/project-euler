
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisable by all of the numbers from 1 to 20?
# Answer: 232792560


def run(numberToTest = 0, maxDivider = 20):
    while True:
        numberToTest += maxDivider  # Counting by the maxDivider maximized how many numbers we can skip

        # Don't need to test by max divider, since every number we test is already divisable by maxDivider
        # Counts backwards in an attempt to be faster
        for divider in range(maxDivider - 1, 1, -1):  

            if numberToTest % divider != 0:  # If numberToTest doesn't divide evenly by divider, try next number   
                break

            elif divider == 2:
                answer : int = numberToTest
                return answer

answer : int = run()
print(answer)
