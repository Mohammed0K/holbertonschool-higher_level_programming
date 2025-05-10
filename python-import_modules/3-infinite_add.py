#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = sum(int(sys.argv[c]) for c in range(1, len(sys.argv)))
    print("{}".format(result))