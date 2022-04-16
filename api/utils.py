from api.constants import ERROR_RESPONSE, MAX_NUM_TO_INT, STATUS_RESPONSE


class ConvertToWords():
    """
    Utility class used to convert a string of numbers to an english 
    word equivalent.
    """
    response = ""
    status = STATUS_RESPONSE.OK
    number = None
    small_digits = {
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
    large_digits = {
        1000000000000000000000: "sextillion",
        1000000000000000000: "quintillion",
        1000000000000000: "quadrillion",
        1000000000000: "trillion",
        1000000000: "billion",
        1000000: "million",
        1000: "thousand",
        100: "hundred",
    }
    zero = "Zero"

    def __init__(self, number):
        self.number = number

        if self.sanitize_number():
            self.convert_to_words()
        else:
            self.status = STATUS_RESPONSE.ERROR

    def convert_to_words(self):
        """
        Converts integer to english word equivalent.
        """
        if self.number == 0:
            self.response = self.zero
        else:
            is_negative = self.number < 0
            if is_negative:
                self.response = f"Negative {self._convert_to_words(self.number * -1)}"\
                    .strip()
            else:
                self.response = self._convert_to_words(self.number).strip()

    def _convert_to_words(self, num):
        """
        Private recursive method to handle convert logic.
        """

        if num < 20:
            return self.small_digits.get(num, "")
        elif 20 <= num <= 99:
            return self.small_digits[num // 10 * 10] + self.small_digits.get(num % 10, "")
        else:
            for large_digit in self.large_digits:
                division = num // large_digit
                if division:
                    return f"{self._convert_to_words(division).strip()} {self.large_digits[large_digit]} {self._convert_to_words(num % large_digit).strip()}"

    def sanitize_number(self):
        """
        Sanitizes input number by checking for a value, validating if it's
        a valid number, and asserting it is between a valid range.

        Returns True if conditions are met, otherwise return False and
        sets the response to the appropriate error message.
        """
        self.number = self.number.strip()
        if not self.number:
            self.response = ERROR_RESPONSE.INVALID_INPUT
            return False

        try:
            self.number = int(self.number)
        except ValueError:
            self.response = ERROR_RESPONSE.INVALID_INPUT
            return False

        if self.number < -MAX_NUM_TO_INT or self.number > MAX_NUM_TO_INT:
            self.response = ERROR_RESPONSE.NUM_OUT_OF_RANGE
            return False

        return True
