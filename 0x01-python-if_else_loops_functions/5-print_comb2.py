#!/usr/bin/python3
for j in range(0, 100):
    if j == 99:
        print(j)
    else:
        print("{:0>2d}".format(j), end=", ")
