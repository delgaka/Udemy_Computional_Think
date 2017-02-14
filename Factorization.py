# -*- coding: utf-8 -*-

from DelgakaChecks import DelgakaChecks

__author__ = "delgaka"


"""
Chalange:

Print all factors number form a givem number

https://github.com/delgaka/Udemy_Computional_Think
"""


# Look for a factor number and print
def look_for_factor(number):
    for i in range(1, int(number) + 1):
        if DelgakaChecks.is_factor(number, i):
            print("%s is factor." % i)


def main():
    num = input("Please, give an integer number: ")
    user_number = DelgakaChecks.input_to_number(num)
    # if the input is not a number, the program will as to run again with a number.
    if DelgakaChecks.is_number(num) and user_number:
        look_for_factor(user_number)
    else:
        print("Please, try again with an integer number!")


if __name__ == '__main__':
    main()

