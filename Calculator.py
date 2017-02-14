# -*- coding: utf-8 -*-

import math
from DelgakaChecks import DelgakaChecks

__author__ = "delgaka"


"""
Chalange:

Square
Cube
square root

https://github.com/delgaka/Udemy_Computional_Think
"""


def square_number(foo):
    return foo ** 2


def cube_number(foo):
    return foo ** 3


def square_root_number(foo):
    return math.sqrt(foo)


def main():
    num = input("Please, type a number: ")
    number = DelgakaChecks.input_to_number_with_float(num)
    if DelgakaChecks.is_number(num) and number:
        print("Square of %s is %s" % (num, square_number(number)))
        print("Cube of %s is %s" % (num, cube_number(number)))
        print("Square root of %s is %s" % (num, square_root_number(number)))
    else:
        print("Please, try again with a number!")


if __name__ == '__main__':
    main()
