#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    lst = []
    try:
        for i in range(list_length):
            a = my_list_1[i]
            b = my_list_2[i]
            try:
                lst.append(a / b)
            except TypeError:
                print("wrong type")
                lst.append(0)
            except ZeroDivisionError:
                print("division by 0")
                lst.append(0)
    except IndexError:
        print("out of range")
        lst.append(0)
    finally:
        return lst
