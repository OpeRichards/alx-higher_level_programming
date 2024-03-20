#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    # last digit if number is positive
    print(last_digit, end='')
    # return last digit
    return last_digit
