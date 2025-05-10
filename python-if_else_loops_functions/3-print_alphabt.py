#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    i = chr(i)
    if i != "e" and i != "q":
        print(i, end="")