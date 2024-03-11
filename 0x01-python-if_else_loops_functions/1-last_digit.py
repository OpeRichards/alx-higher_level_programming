#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = str(number)
last_digit = digit[-1]
last_digit = int(last_digit)
if last_digit > 5:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif last_digit == 0:
    print(f'Last digit of {number} and is 0')
else:
    print(f'Last digit of {number} is {last_digit} and is less than 6')
