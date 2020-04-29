#!/usr/bin/python3
o = 2
t = 0
print("01", end='')
while (t < 9):
    while (o < 10):
        print(", {}{}".format(t, o), end='')
        o = o + 1
    t = t + 1
    o = t + 1
print('\n', end='')
