#!/usr/bin/python3
def uppercase(str):
    for elem in str:
        if ord(elem) > 96 and ord(elem) < 123:
            elem = (chr(ord(elem) - 32))
        print(elem, end='')
    print('\n', end='')
