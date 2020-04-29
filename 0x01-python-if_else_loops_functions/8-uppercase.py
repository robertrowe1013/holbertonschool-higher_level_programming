#!/usr/bin/python3
def uppercase(str):
    for elem in str:
        if ord(elem) > 96 and ord(elem) < 123:
            print("{}".format(chr(ord(elem) - 32)), end='')
        else:
            print("{}".format(elem), end='')
