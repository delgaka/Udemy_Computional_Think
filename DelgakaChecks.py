# -*- coding: utf-8 -*-


__author__ = "delgaka"


"""
Chalange:

Print all factors number form a givem number

https://github.com/delgaka/Udemy_Computional_Think
"""


class DelgakaChecks():
    # convert input to a number
    @staticmethod
    def input_to_number(user_input):
        if DelgakaChecks.is_number(user_input):
            # if the float number less your int conversion is greater than 0.0 is a float number
            if (float(user_input) - int(float(user_input))) > 0.0:
                # we don't want a float number to iterate
                return False
            else:
                # in python3 we need to convert a explicit float to an int number
                return int(float(user_input))
        return False

    # convert input to a number
    @staticmethod
    def input_to_number_with_float(user_input):
        if DelgakaChecks.is_number(user_input):
            # if the float number less your int conversion is greater than 0.0 is a float number
            if (float(user_input) - int(float(user_input))) > 0.0:
                return float(user_input)
            else:
                # in python3 we need to convert a explicit float to an int number
                return int(float(user_input))
        return False

    # Check if the variable is a number (float or integer)
    @staticmethod
    def is_number(user_number):
        try:
            # I only need to test a float conversion
            float(user_number)
            return True
        except ValueError:
            return False

    # Check if the number is a factor
    @staticmethod
    def is_factor(number, n):
        if number % n == 0:
            return True
        else:
            return False
