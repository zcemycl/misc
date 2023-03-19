'''
Roman numerals are a numeral system that originated 
in ancient Rome and remained the usual way of writing
numbers throughout Europe well into the Late Middle 
Ages. Roman numerals are based on seven symbols:

Symbol-Value
- I = 1
- V = 5
- X = 10
- L = 50
- C = 100
- D = 500
- M = 1000

Roman Numerals System:
1. You add the value of all the symbols: so II is 2, LXVI is 66, etc.
2. There may not be more than three of the same characters in a row.
3. Subtraction is used in place of >3 repetitions: e.g.
  - rather than writing IIII for 4, you write IV (for 5 minus 1); and
  - instead of writing LXXXX for 90, you write XC.
4. Symbols must be ordered by descending value except when subtracting.

Examples:
MMXVIII = 2018
MCMXCIX = 1999

Task:
Write a function that takes as input a correctly formatted Roman numeral string and returns an integer
with the equivalent decimal number.
'''

def convert_roman_to_int(roman_string: str) -> int:
    map_roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = map_roman_int[roman_string[len(roman_string)-1]]
    for i in range(len(roman_string)-2,-1,-1):
        result += -map_roman_int[roman_string[i]] if map_roman_int[roman_string[i]] < map_roman_int[roman_string[i+1]] else map_roman_int[roman_string[i]]
    return result

if __name__ == "__main__":
    for test_case in ["MMXVIII", "MCMXCIX", "IV", "III", "MM", "DD"]:
        print(convert_roman_to_int(test_case))