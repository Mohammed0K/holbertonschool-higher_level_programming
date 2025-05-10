#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden
    list = dir(hidden)
    for c in range(len(list)):
        if(list[c][0] != "_"):
            print(list[c])