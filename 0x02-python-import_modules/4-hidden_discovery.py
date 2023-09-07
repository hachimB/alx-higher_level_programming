#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for item in names:
        item.sort()
        if not item.startswith("__"):
            print(item)
