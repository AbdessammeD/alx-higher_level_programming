#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(i, end="\n")
    else:
        print("0{}".format(i) if i < 10 else "{}".format(i), end=", ")
