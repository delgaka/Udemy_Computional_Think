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


def square_number(number):
    return number ** 2


def cube_number(number):
    return number ** 3


def square_root_number(number):
    return math.sqrt(number)


if __name__ == '__main__':
    num = input("Please, type a number: ")
    print "Square of %s is %s" % (num, square_number(num))
    print "Cube of %s is %s" % (num, cube_number(num))
    print "Square root of %s is %s" % (num, square_root_number(num))
