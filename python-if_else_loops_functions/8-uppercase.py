#!/usr/bin/python3
def uppercase(str):
    """Convert a string to uppercase."""
    return str.upper()


if __name__ == "__main__":
    uppercases = "best"
    uppercasese = "Best School 98 Battery street"
    print("{}".format(uppercase(uppercases)))
    print("{}".format(uppercase(uppercasese)))
