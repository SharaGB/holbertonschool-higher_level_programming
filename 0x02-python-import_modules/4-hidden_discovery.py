#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for arg in dir(hidden_4):
        if arg != "__":
            print("{:s}".format(arg))
