#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    co = len(sys.argv) - 1
    if co == 0:
        print("0 arguments.")
    elif co == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(co))
    for i in range(co):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
