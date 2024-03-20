#!/usr/bin/python3
def print_last_digit(number):
    # last digit if number is positive
    if number > 0:
        return number % 10
    else:
        # last digit if number is negative
        return number % (-10)
