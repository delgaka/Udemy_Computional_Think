# -*- coding: utf-8 -*-

import math

__author__ = "delgaka"


"""
Chalange:

Square
Cube
square root

https://github.com/delgaka
"""


# convert input to a number
def input_to_number(user_input):
    if is_number(user_input):
        # if the float number less your int conversion is greater than 0.0 is a float number
        if (float(user_input) - int(float(user_input))) > 0.0:
            return float(user_input)
        else:
            # in python3 we need to convert a explicit float to an int number
            return int(float(user_input))
    return False


# Check if the variable is a number (float or integer)
def is_number(user_number):
    try:
        # I only need to test a float conversion
        float(user_number)
        return True
    except ValueError:
        return False


def square_number(foo):
    return foo ** 2


def cube_number(foo):
    return foo ** 3


def square_root_number(foo):
    return math.sqrt(foo)


def main():
    num = input("Please, type a number: ")
    number = input_to_number(num)
    if is_number(num) and number:
        print("Square of %s is %s" % (num, square_number(number)))
        print("Cube of %s is %s" % (num, cube_number(number)))
        print("Square root of %s is %s" % (num, square_root_number(number)))
    else:
        print("Please, try again with a number!")


if __name__ == '__main__':
    main()
