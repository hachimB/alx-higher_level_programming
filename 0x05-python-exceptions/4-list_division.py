#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list2 = []
    for i in range(list_length):
        try:
            x = my_list_1[i]
            y = my_list_2[i]

            if not (isinstance(x, (int, float)) and
                    isinstance(y, (int, float))):
                print("wrong type")
                list2.append(0)
                continue

            if y == 0:
                print("division by zero")
                list2.append(0)
                continue
            result = x / y
            list2.append(result)

        except IndexError:
            print("out of range")
            list2.append(0)
        finally:
            list2 = list2
    return list2
