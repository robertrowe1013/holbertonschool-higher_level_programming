#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = digit * -1
print("Last digit of {} is {}".format(number, digit), end=' ')
if digit > 5:
    print("and is greater than 5")
elif digit is 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
