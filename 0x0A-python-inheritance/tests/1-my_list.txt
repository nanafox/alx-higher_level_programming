>>> MyList = __import__('1-my_list').MyList


==== Instantiate and use (Expected general use) ====

>>> my_list = MyList()
>>> my_list.append(4)
>>> my_list
[4]
>>> my_list.append(1)
>>> my_list.append(2)
>>> my_list.append(3)

>>> my_list
[4, 1, 2, 3]

# Print the list in sorted order
>>> my_list.print_sorted()
[1, 2, 3, 4]

# Ensure the original list has not changed
>>> my_list
[4, 1, 2, 3]


==== Another way of instantiating the list ====

>>> my_list2 = MyList([10, 3, 34, 2, 10, -1])
>>> my_list2
[10, 3, 34, 2, 10, -1]
>>> my_list2.print_sorted()
[-1, 2, 3, 10, 10, 34]


==== Perform slicing ====

>>> my_list[0:2]
[4, 1]
>>> my_list2[-3:]
[2, 10, -1]


==== Test the pop method ====

>>> my_list2.pop()
-1

# check to ensure the element was really popped
>>> my_list2
[10, 3, 34, 2, 10]


==== Tests element modification ====

>>> my_list2[0] = 12
>>> my_list2
[12, 3, 34, 2, 10]


==== Test list concatenation ====

>>> add_list = MyList(my_list + my_list2)
>>> add_list
[4, 1, 2, 3, 12, 3, 34, 2, 10]


==== Sort the list in place ====

# print with the method first
>>> add_list.print_sorted()
[1, 2, 2, 3, 3, 4, 10, 12, 34]

>>> add_list.sort()
>>> add_list
[1, 2, 2, 3, 3, 4, 10, 12, 34]


==== Delete an element with the `del` keyword ====

>>> del add_list[-2]
>>> add_list
[1, 2, 2, 3, 3, 4, 10, 34]


==== Test the count method ====

>>> add_list.count(3)
2
>>> add_list.count(45)
0

==== Test IndexError ====

>>> add_list[len(add_list)]
Traceback (most recent call last):
...
IndexError: list index out of range


==== Delete the list ====

>>> del add_list
>>> add_list
Traceback (most recent call last):
...
NameError: name 'add_list' is not defined

>>> add_list.print_sorted()
Traceback (most recent call last):
...
NameError: name 'add_list' is not defined

==== Invalid argument ====

>>> new_list = MyList(3)
Traceback (most recent call last):
...
TypeError: 'int' object is not iterable


==== Test Negative Numbers ====

>>> neg_list = MyList([-4, -2, -1, -9, -3, -5])
>>> neg_list.insert(0, -98)
>>> neg_list.print_sorted()
[-98, -9, -5, -4, -3, -2, -1]
>>> neg_list
[-98, -4, -2, -1, -9, -3, -5]


==== Test same numbers ====

>>> same_numbers = MyList([0, 0, 0, 0])
>>> same_numbers.print_sorted()
[0, 0, 0, 0]


==== Test empty list ====

>>> empty = MyList()
>>> empty.print_sorted()
[]
