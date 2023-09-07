#!/usr/bin/python3
if __name__ == "__main__":
    from importlib import import_module
    module_name = "hidden_4"
    module_path = f"{module_name}.pyc"
    module = import_module(module_name, module_path)
    names = dir(module)
    names.sort()
    for item in names:
        if not item.startswith("__"):
            print(item)
