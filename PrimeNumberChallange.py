# -*- coding: utf-8 -*-
import time

from DelgakaChecks import DelgakaChecks

__author__ = "delgaka"


"""
Chalange:

Print all factors number form a givem number

https://github.com/delgaka/Udemy_Computional_Think
"""


def define_the_prime_numbers(max_number):
    is_prime = [True] * (max_number + 1)
    is_prime[0] = False
    is_prime[1] = False
    list_of_primes = []
    for i in range(2, max_number + 1):
        if is_prime[i]:
            list_of_primes.append(i)

        for x in range(i*2, max_number + 1, i):
            is_prime[x] = False

    return list_of_primes


def main():
    max_number = input("Please, give an max integer number to find the : ")
    user_number = DelgakaChecks.input_to_number(max_number)
    # if the input is not a number, the program will as to run again with a number.
    start_time = time.time()
    if DelgakaChecks.is_number(max_number) and user_number:
        list_of_primes = define_the_prime_numbers(user_number)
        print("These are the prime numbers:")
        print(list_of_primes)
        print(len(list_of_primes))
    else:
        print("Please, try again with an integer number!")

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()