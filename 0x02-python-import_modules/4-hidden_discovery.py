#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all names in the module"""
    import hidden_4

    mod_names = dir(hidden_4)

    for i in mod_names:
        if i[:2] != '__':
            print(i)
