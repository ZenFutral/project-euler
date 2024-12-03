# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
# 
# Answer: 
# Average Runtime: 

from custom_modules.script_report import reporter

num_name_dict: dict[str, str] = {  # Unique number names
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety"
}

def getdesired_digits(target_idx: int, number: str) -> str:
    desired_digits: str = number[target_idx]

    return desired_digits

def getOnesAndTens(number: str) -> int:
    digit_str_len: int = 0
    num_as_string: str = ''
    ones_digit: str = getdesired_digits(-1, number)
    tens_digit: str = "0"

    if len(number) > 1:
        tens_digit = getdesired_digits(-2, number)
    
    else:
        num_as_string = num_name_dict[ones_digit]
    
    if tens_digit != "0":
        compositNumber = tens_digit[0] + ones_digit

        if compositNumber in num_name_dict.keys():
            num_as_string = num_name_dict[compositNumber]

        else:
            num_as_string = num_name_dict[tens_digit + "0"]
            num_as_string = num_as_string + num_name_dict[ones_digit]

    print(num_as_string)
    digit_str_len = len(num_as_string)
    return digit_str_len
    
def getHundredsAndUp(number: str, tenToThePowerOf: int) -> int:
    idx = tenToThePowerOf - 2    # translating 10^x to list[idx] where idx=x-1

    powerStrings: list[str] = ['Hundred', 'Thousand']
    digit_str_len: int = 0
    digits: str = getdesired_digits(idx * -1, number)
    print(digits)

    if digits == "0":
        return 0

    else:
        num_as_string: str = num_name_dict[digits] + powerStrings[idx]
        digit_str_len += len(num_as_string)
        print(num_as_string)
    
    return digit_str_len

def main() -> int:
    upper_bound:      int = 1000
    total_char_count: int = 0

    for count in range(1, upper_bound + 1):
        num_as_str: str = str(count)
    
        if len(num_as_str) >= 4:    # Thousands   
            thousandsLetterCount: int = getHundredsAndUp(num_as_str, tenToThePowerOf=3)
            total_char_count += thousandsLetterCount

        if len(num_as_str) >= 3:    # Hundreds
            hundredsLetterCount: int = getHundredsAndUp(num_as_str, tenToThePowerOf=2)
            total_char_count += hundredsLetterCount

        onesAndTensLetterCount: int = getOnesAndTens(num_as_str)
        total_char_count += onesAndTensLetterCount

        if (len(num_as_str) >= 3) and (onesAndTensLetterCount > 0):
            total_char_count += 3
            print("And")

    answer: int = total_char_count
    return answer

reporter(main_function= main)