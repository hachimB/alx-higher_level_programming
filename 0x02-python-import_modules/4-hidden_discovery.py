#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    # Specify the file path to the compiled module
    module_name = "hidden_4"
    module_path = f"{module_name}.pyc"
    # Create a module spec from the file location
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    # Load the module from the spec
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    names = dir(module)
    names.sort()
    for item in names:
        if not item.startswith("__"):
            print(item)
