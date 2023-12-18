#!/usr/bin/python3


def list_division(my_list_1: list, my_list_2: list, list_length: int) -> list:
    """
    Returns a list of quotients from two lists after dividing
    element by element

    Args:
        my_list_1 (list): the first list
        my_list_2 (list): the second list
        list_length (int): the length of the new list

    Returns:
        list: a list of quotients
    """
    quotients = []

    for i in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except (ValueError, TypeError):
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            quotients.append(quotient)

    return quotients
