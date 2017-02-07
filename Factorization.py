# -*- coding: utf-8 -*-


__author__ = "delgaka"


"""
Chalange:

Print all factors number form a givem number

https://github.com/delgaka
"""


# convert input to a number
def input_to_number(user_input):
    if is_number(user_input):
        # if the float number less your int conversion is greater than 0.0 is a float number
        if (float(user_input) - int(float(user_input))) > 0.0:
            # we don't want a float number to iterate
            return False
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
            print("%s is factor." % i)


def main():
    num = input("Please, give an integer number: ")
    user_number = input_to_number(num)
    # if the input is not a number, the program will as to run again with a number.
    if is_number(num) and user_number:
        look_for_factor(user_number)
    else:
        print("Please, try again with an integer number!")


if __name__ == '__main__':
    main()

