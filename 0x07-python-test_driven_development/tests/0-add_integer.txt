>>> add_integer = __import__('0-add_integer').add_integer

==== Test for expected behaviour ====

>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(-2, 100.3)
98
>>> add_integer(0)
98
>>> add_integer(float('8.9'))
106

==== Now let's check for edge cases ====

Edge case 1: Passing strings as arguments
>>> add_integer(4, "School")
Traceback (most recent call last):
...
TypeError: b must be an integer
>>> add_integer("Best", "School")
Traceback (most recent call last):
...
TypeError: a must be an integer

Edge case 2: Passing None as an argument
>>> add_integer(None)
Traceback (most recent call last):
...
TypeError: a must be an integer
>>> add_integer(12, None)
Traceback (most recent call last):
...
TypeError: b must be an integer

# Edge case 3: Passing infinity as an argument (Tests for overflow)
>>> add_integer(float('inf'))
Traceback (most recent call last):
...
OverflowError: cannot convert float infinity to integer
>>> add_integer(76, float('inf'))
Traceback (most recent call last):
...
OverflowError: cannot convert float infinity to integer

# Edge 4: Check for the NaN type
>>> add_integer(float('nan'))
Traceback (most recent call last):
...
ValueError: cannot convert float NaN to integer

# Edge 5: Try different sequence data types and others
>>> add_integer([4, 3])
Traceback (most recent call last):
...
TypeError: a must be an integer
>>> add_integer(float('School'))
Traceback (most recent call last):
...
ValueError: could not convert string to float: 'School'

# Edge case 6: Positional argument missing
>>> add_integer()
Traceback (most recent call last):
...
TypeError: add_integer() missing 1 required positional argument: 'a'

==== ALX-based tests ====

>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(-2, 100.3)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
...
TypeError: b must be an integer
>>> add_integer("Best", "School")
Traceback (most recent call last):
...
TypeError: a must be an integer
>>> add_integer(None)
Traceback (most recent call last):
...
TypeError: a must be an integer
>>> add_integer(float('inf'))
Traceback (most recent call last):
...
OverflowError: cannot convert float infinity to integer
>>> add_integer(float('nan'))
Traceback (most recent call last):
...
ValueError: cannot convert float NaN to integer
