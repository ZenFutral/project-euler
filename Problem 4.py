# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609

def defineRange(digitCount : int):
    lowerstNumberStr : str = "1"
    highestNumberStr : str = "9"

    for i in range(digitCount - 1):
        lowerstNumberStr += "0"
        highestNumberStr += "9"

    lowestNumber : int = int(lowerstNumberStr)
    highestNumber : int = int(highestNumberStr)

    bounds : tuple[int] = (lowestNumber, highestNumber)
    return bounds

def testIfPal(number : int):
    numberStr : str = str(number)

    if numberStr == numberStr[::-1]:
        return True
    
    else:
        return False

def run():
    palList : list[int] = []

    bounds : tuple[int] = defineRange(3) # Creates our lowest and highest number from digit limit
    lowestNumber : int = bounds[0] - 1 # -1 to allow for exlusive ranges
    highestNumber : int = bounds[1]

    primaryRange : range = range(highestNumber, lowestNumber, -1) # Start testing numbers starting from the largest
    for primaryNumber in primaryRange:
        secondaryRange : range = range(primaryNumber, lowestNumber, -1) # Removes duplicate operations

        for secondaryNumber in secondaryRange:
            numberToTest : int = primaryNumber * secondaryNumber

            if testIfPal(numberToTest): # If the numberToTest is a pal, add to our list
                palList.append(numberToTest)
    
    answer : int = max(palList)
    return answer

answer : int = run()
print(answer)
