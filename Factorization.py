# -*- coding: utf-8 -*-


__author__ = "delgaka"


"""
Chalange:

Print all factors number form a givem number

https://github.com/delgaka
"""


# Check if the variable is a number (float or integer)
def is_number(number):
    try:
        float(number)
        int(number)
        return True
    except ValueError:
        return False


# Check if the number is a factor
def is_factor(number, n):
    if number % n == 0:
        return True
    else:
        return False


# Look for a factor number and print
def look_for_factor(number):
    for i in range(1, int(number) + 1):
        if is_factor(number, i):
            print "%s is factor." % i
        else:
            print "%i is not a factor." % i


if __name__ == '__main__':
    num = input("Please, give a number: ")
    # if the input is not a number, the program will as to run again with a number.
    if is_number(num):
        look_for_factor(num)
    else:
        print "Please, try again with a number!"

