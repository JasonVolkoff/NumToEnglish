from types import SimpleNamespace

MAX_NUM_TO_INT = 10**21
ERROR_RESPONSE = SimpleNamespace(
    INVALID_INPUT="Please enter a valid whole number. Example: '123'",
    NUM_OUT_OF_RANGE="Input out of range. Please use whole numbers between -10^21 to 10^21"
)
STATUS_RESPONSE = SimpleNamespace(
    OK="ok",
    ERROR="error"
)
SMALL_DIGITS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "fourty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninty",
}
LARGE_DIGITS = {
    1000000000000000000000: "sextillion",
    1000000000000000000: "quintillion",
    1000000000000000: "quadrillion",
    1000000000000: "trillion",
    1000000000: "billion",
    1000000: "million",
    1000: "thousand",
    100: "hundred",
}
ZERO = "Zero"
