#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    names.sort()
    for item in names:
        if not item.startswith("__"):
            print(item)
